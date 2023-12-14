#include <algorithm>
#include <string>
#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <signal.h>
#include <unistd.h>
#include <cstdlib>

pid_t __reactive_pid;
int __reactive_input, __reactive_output;

int reactive_start(std::string command) {
  int pipe_c2p[2], pipe_p2c[2];

  signal(SIGPIPE, SIG_IGN);
  if (pipe(pipe_c2p) < 0 || pipe(pipe_p2c) < 0) {
    fprintf(stderr, "pipe: failed to open pipes\n");
    return 1;
  }
  if ((__reactive_pid = fork()) < 0) {
    fprintf(stderr, "fork: failed to fork\n");
    return 1;
  }
  if (__reactive_pid == 0) {
    close(pipe_p2c[1]); close(pipe_c2p[0]);
    dup2(pipe_p2c[0], 0); dup2(pipe_c2p[1], 1);
    close(pipe_p2c[0]); close(pipe_c2p[1]);
    exit(system(command.c_str()) ? 1 : 0);
  }
  close(pipe_p2c[0]); close(pipe_c2p[1]);
  __reactive_input = pipe_p2c[1];
  __reactive_output = pipe_c2p[0];
  return 0;
}

void reactive_end() {
  int status;
  close(__reactive_input);
  waitpid(__reactive_pid, &status, WUNTRACED);
}

void reactive_write(std::string buf) {
  write(__reactive_input, buf.c_str(), buf.size());
}

std::string reactive_read(int max_len = 100000) {
  static char buf[1024]; static int len = 0; std::string result;
  while (static_cast<int>(result.size()) < max_len) {
    if (!len) {
      len = read(__reactive_output, buf,
          std::min(1000, (int)(max_len - result.size())));
      if (!len) return result;
    }
    char *pos = (char *)memchr(buf, '\n', len);
    if (pos) {
      result += std::string(buf, pos - buf + 1);
      memmove(buf, pos + 1, len - (pos + 1 - buf));
      len -= pos - buf + 1;
      return result;
    } else {
      result += std::string(buf, len);
      len = 0;
    }
  }
  return result;
}
