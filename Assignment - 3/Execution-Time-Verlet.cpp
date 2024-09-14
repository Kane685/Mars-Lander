#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

using namespace std;

int main() {
  double balance[] = {0.1, 0.01, 0.001, 0.0001, 0.00001};
  for (int i = 0; i <= 4; i++){
  // start time
  auto start = chrono::high_resolution_clock::now();

  // declare variables
  double m, k, x, v, t_max, dt, t, a;
  vector<double> t_list, x_list, v_list;

  // mass, spring constant, initial position and velocity
  m = 1;
  k = 1;
  x = 0;
  v = 1;

  // simulation time and timestep
  t_max = 100;
  dt = balance[i];

  // Euler integration
  for (t = 0; t <= t_max; t = t + dt) {

    // append current state to trajectories
    t_list.push_back(t);
    x_list.push_back(x);
    v_list.push_back(v);

    // calculate new position and velocity
    if (t == 0){
      a = - k * x / m;
      x = x + dt * v + (dt * dt) * a;
      v = (x - x_list[x_list.size()-1]) / dt;
    }else{
      a = - k * x / m;
      x = 2 * x - x_list[x_list.size()-2]+ (dt * dt) * a;
      v = (x - x_list[x_list.size()-1]) / dt;
    }
  }
  // end time
  auto end = chrono::high_resolution_clock::now();

  // execution time
  chrono::duration<double, std::milli> elapsed = end - start;
  cout << "Execution time - Verlet: " << elapsed.count() / 1000 << " second" << " when dt is :" << dt << endl;
  }
  // Write the trajectories to file
  // ofstream fout;
  // fout.open("trajectories.txt");
  // if (fout) { // file opened successfully
  //   for (int i = 0; i < t_list.size(); i = i + 1) {
  //     fout << t_list[i] << ' ' << x_list[i] << ' ' << v_list[i] << endl;
  //   }
  // } else { // file did not open successfully
  //   cout << "Could not open trajectory file for writing" << endl;
  // }

  /* The file can be loaded and visualised in Python as follows:

  import numpy as np
  import matplotlib.pyplot as plt
  results = np.loadtxt('trajectories.txt')
  plt.figure(1)
  plt.clf()
  plt.xlabel('time (s)')
  plt.grid()
  plt.plot(results[:, 0], results[:, 1], label='x (m)')
  plt.plot(results[:, 0], results[:, 2], label='v (m/s)')
  plt.legend()
  plt.show()

  */
}
