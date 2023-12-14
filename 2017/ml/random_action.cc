#include <iostream>
#include <vector>


void get_observation(std::vector<double>& obs, bool& done) {
  std::string stat;
  std::cin >> stat;
  if (stat == "obs") {
    obs.resize(4);
    for (int i = 0; i < 4; ++i) std::cin >> obs[i];
    done = false;
  } else if (stat == "done") {
    done = true;
  }
}

int main() {
  for (int episode = 1; episode <= 10; ++episode) {
    std::cerr << "###### Episode " << episode << " ######" << std::endl;
    std::cout << "r" << std::endl;
    std::vector<double> obs;
    bool done;
    get_observation(obs, done);

    std::cerr << "Initial observation:";
    for (auto& x : obs) std::cerr << x << " ";
    std::cerr << std::endl;

    for (int step = 0; ; ++step) {
      int action = (rand() % 2) ? 1 : -1;
      std::cout << "s " << action << std::endl;
      get_observation(obs, done);

      std::cerr << "Step " << step << " :";
      for (auto& x : obs) std::cerr << x << " ";
      std::cerr << std::endl;

      if (done) break;
    }
  }
  std::cout << "q" << std::endl;
}
