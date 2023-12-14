// Some part of this code is based on CartPole environment in OpenAi Gym.
// Some parameters are modified to adjust the difficulty of the problem.
// https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
#include <string>
#include <cstring>

#include "reactive.hpp"
#include <cmath>
#include <ctime>
#include <sstream>
#include <iostream>
#include <iomanip>

#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif

std::string toString(double d) {
  std::ostringstream oss;
  oss<<std::setprecision(12)<<d;
  return oss.str();
}

void strip(std::string &s) {
  while(s.size()>0 && (s[s.size()-1]=='\n' || s[s.size()-1]=='\r'))
    s = s.substr(0, s.size()-1);
}

void invalid(std::string command) {
  std::cout << "[WARNING] Invalid command: " << command << std::endl;
}

constexpr double gravity = 9.8;
constexpr double masscart = 1.0;
constexpr double masspole = 0.1;
constexpr double total_mass = (masspole + masscart);
constexpr double length = 0.5;
constexpr double polemass_length = (masspole * length);
constexpr double force_mag = 10.0;
constexpr double tau = 0.02;
constexpr double theta_threshold_radians = 12 * 2 * M_PI / 360;
constexpr double x_threshold = 2.4;

double x;
double x_dot;
double theta;
double theta_dot;

void reset() {
  x         = (rand() % 1000 / 1000.0 - 0.5) * 2.0 * 1.20;
  x_dot     = (rand() % 1000 / 1000.0 - 0.5) * 2.0 * 0.15;
  theta     = (rand() % 1000 / 1000.0 - 0.5) * 2.0 * 0.15;
  theta_dot = (rand() % 1000 / 1000.0 - 0.5) * 2.0 * 0.15;
}

void step(int action) {
  double force = force_mag * action;
  double costheta = cos(theta);
  double sintheta = sin(theta);
  double temp = (force + polemass_length * theta_dot * theta_dot * sintheta) / total_mass;
  double thetaacc = (gravity * sintheta - costheta* temp) / (length * (4.0/3.0 - masspole * costheta * costheta / total_mass));
  double xacc  = temp - polemass_length * thetaacc * costheta / total_mass;

  x = x + tau * x_dot;
  x_dot = x_dot + tau * xacc;
  theta = theta + tau * theta_dot;
  theta_dot = theta_dot + tau * thetaacc;
}

bool done() {
  return x < -x_threshold
    || x > x_threshold
    || theta < -theta_threshold_radians
    || theta > theta_threshold_radians;
}

void interaction() {
  for(;;) {
    std::string line = reactive_read();
    strip(line);
    if(line.empty()) {
      invalid(line);
      return;
    }
    if(line[0]!='r' && line[0]!='s' && line[0]!='q') {
      invalid(line);
      return;
    }

    if(line[0] == 'r') {
      reset();
      reactive_write("obs "+toString(x) + " " + toString(x_dot) + " " + toString(theta) + " " + toString(theta_dot) + "\n");
      continue;
    } else if (line[0] == 's'){
      std::istringstream iss(line.substr(1));
      int action;
      iss >> action;
      if (action != +1 && action != -1) {
        invalid(line);
        return;
      }

      step(action);
      if (done()) {
        reactive_write("done\n");
      } else {
        reactive_write("obs "+toString(x) + " " + toString(x_dot) + " " + toString(theta) + " " + toString(theta_dot) + "\n");
      }
    } else if (line[0] == 'q') {
      return;
    }
  }
}

int main(int argc,char **argv) {
  srand(time(NULL));
  reactive_start(argv[1]);
  reset();
  interaction();
  reactive_end();
  return 0;
}
