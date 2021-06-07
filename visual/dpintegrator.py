from abstractinterface import AbstractIntegrator
import time


class DormandPrinceIntegrator(AbstractIntegrator):
    def __iter__(self):
        return self

    def __init__(self, model, step, precision, initial_time, final_time):
        super().__init__(model, step, precision, initial_time, final_time)
        self.bc = [0, 1 / 5, 3 / 10, 4 / 5, 8 / 9, 1, 1]  # Butcher column
        self.bt = [[1 / 5],
                   [3 / 40, 9 / 40],
                   [44 / 45, -56 / 15, 32 / 9],
                   [19372 / 6561, -25360 / 2187, 64448 / 6561, -212 / 729],
                   [9017 / 3168, -355 / 33, 46732 / 5247, 49 / 176, -5103 / 18656],
                   [35 / 384, 0, 500 / 1113, 125 / 192, -2187 / 6784, 11 / 84]]  # Butcher table
        self.order4coefficient = [35 / 384, 0, 500 / 1113, 125 / 192, -2187 / 6784, 11 / 84]
        self.order5coefficient = [5179 / 57600, 0, 7571 / 16695, 393 / 640, -92097 / 339200, 187 / 2100, 1 / 40]

        self.order5solution = list(self.const.model.InitialValues)

    def k_calculation(self, step):
        K = [[], [], [], []]
        param = [[], [], [], [], [], [], []]

        for j in range(self.const.equations_number):
            param[0].append(self.order5solution[j])
        for i in range(self.const.equations_number):
            K[i].append(self.const.model.RightParts[i](self.t + self.bc[0] * step, param[0]))

        for j in range(self.const.equations_number):
            param[1].append(self.order5solution[j]
                            + self.bt[0][0] * K[j][0] * step)
        for i in range(self.const.equations_number):
            K[i].append(self.const.model.RightParts[i](self.t + self.bc[1] * step, param[1]))

        for j in range(self.const.equations_number):
            param[2].append(self.order5solution[j]
                            + (self.bt[1][0] * K[j][0] + self.bt[1][1] * K[j][1]) * step)
        for i in range(self.const.equations_number):
            K[i].append(self.const.model.RightParts[i](self.t + self.bc[2] * step, param[2]))

        for j in range(self.const.equations_number):
            param[3].append(self.order5solution[j]
                            + (self.bt[2][0] * K[j][0] + self.bt[2][1] * K[j][1] + self.bt[2][2] * K[j][2]) * step)
        for i in range(self.const.equations_number):
            K[i].append(self.const.model.RightParts[i](self.t + self.bc[3] * step, param[3]))

        for j in range(self.const.equations_number):
            param[4].append(self.order5solution[j]
                            + (self.bt[3][0] * K[j][0] + self.bt[3][1] * K[j][1] + self.bt[3][2] * K[j][2]
                               + self.bt[3][3] * K[j][3]) * step)
        for i in range(self.const.equations_number):
            K[i].append(self.const.model.RightParts[i](self.t + self.bc[4] * step, param[4]))

        for j in range(self.const.equations_number):
            param[5].append(self.order5solution[j]
                            + (self.bt[4][0] * K[j][0] + self.bt[4][1] * K[j][1]
                               + self.bt[4][2] * K[j][2] + self.bt[4][3] * K[j][3] + self.bt[4][4] * K[j][4]) * step)
        for i in range(self.const.equations_number):
            K[i].append(self.const.model.RightParts[i](self.t + self.bc[5] * step, param[5]))

        for j in range(self.const.equations_number):
            param[6].append(self.order5solution[j]
                            + (self.bt[5][0] * K[j][0] + self.bt[5][1] * K[j][1]
                               + self.bt[5][2] * K[j][2] + self.bt[5][3] * K[j][3]
                               + self.bt[5][4] * K[j][4] + self.bt[5][5] * K[j][5]) * step)
        for i in range(self.const.equations_number):
            K[i].append(self.const.model.RightParts[i](self.t + self.bc[6] * step, param[6]))

        return K

    def solution_calculation(self, step, k):
        theta = (self.t_out - self.t + step) / step
        b = [theta * (1 + theta * (-1337 / 480 + theta * (1039 / 360 + theta * (-1163 / 1152)))),
             0,
             100 * (theta ** 2) * (1054 / 9275 + theta * (-4682 / 27825 + theta * (379 / 5565))) / 3,
             -5 * (theta ** 2) * (27 / 40 + theta * (-9 / 5 + theta * (83 / 96))) / 2,
             18225 * (theta ** 2) * (-3 / 250 + theta * (22 / 375 + theta * (-37 / 600))) / 848,
             -22 * (theta ** 2) * (-3 / 10 + theta * (29 / 30 + theta * (-17 / 24))) / 7]
        solution = list(self.order5solution)
        for i in range(self.const.equations_number):
            for j in range(0, 6):
                solution[i] += step * b[j] * k[i][j]
        return solution

    def y4_calculation(self, step, k):
        Y4 = []
        for solution_index in range(self.const.equations_number):
            Y4.append(self.order5solution[solution_index] + step *
                      (self.order4coefficient[0] * k[solution_index][0] +
                       self.order4coefficient[1] * k[solution_index][1] +
                       self.order4coefficient[2] * k[solution_index][2] +
                       self.order4coefficient[3] * k[solution_index][3] +
                       self.order4coefficient[4] * k[solution_index][4] +
                       self.order4coefficient[5] * k[solution_index][5]))
        return Y4

    def y5_calculation(self, step, k):
        Y5 = []
        for solution_index in range(self.const.equations_number):
            Y5.append(self.order5solution[solution_index] + step *
                      (self.order5coefficient[0] * k[solution_index][0] +
                       self.order5coefficient[1] * k[solution_index][1] +
                       self.order5coefficient[2] * k[solution_index][2] +
                       self.order5coefficient[3] * k[solution_index][3] +
                       self.order5coefficient[4] * k[solution_index][4] +
                       self.order5coefficient[5] * k[solution_index][5] +
                       self.order5coefficient[6] * k[solution_index][6]))
        return Y5

    def local_error_calculation(self, step, y4, y5):
        temp_sum = 0
        for i in range(self.const.equations_number):
            temp_sum += (step * (y4[i] - y5[i]) /
                         max(1e-5, abs(y4[i]), abs(self.order5solution[i]), self.const.rounding_error)) ** 2
        local_error = (temp_sum / self.const.equations_number) ** 0.5
        return local_error

    def __next__(self):
        if self.t < self.const.ft:
            print(self.t)
            time.sleep(0.001)
            step = self.new_step

            K = list(self.k_calculation(step))

            Y4 = self.y4_calculation(step, K)
            Y5 = self.y5_calculation(step, K)

            local_error = self.local_error_calculation(step, Y4, Y5)

            self.new_step = step / max(0.1, min(5, ((local_error / self.const.precision) ** 0.2) / 0.9))

            if local_error > self.const.precision:
                return 0
            
            else:
                Result = []
                while (self.t_out < self.t + step) and (self.t_out <= self.const.ft):
                    solution = self.solution_calculation(step, K)
                    Result.append([self.t_out, solution])
                    self.t_out += self.const.sampling_increment

                self.order5solution = list(Y5)
                self.t += step
                return Result
