import numpy as np
import time


class PID:
    def __init__(self, K_p=0.0, K_i=0.0, K_d=0.0, integral_limit=None):
        """Constructor
        Args:
            K_p (float): The proportional gain
            K_i (float): The integral gain
            K_d (float): The derivative gain
            integral_limit (float, optional): The integral limit
        """
        self.K_p = K_p
        self.K_i = K_i
        self.K_d = K_d
        self.integral_limit = integral_limit
        self.integral_error = 0

        self.reset()

    def reset(self):
        """Reset the PID controller"""
        self.last_error = 0.0
        self.integral = 0.0
        self.last_time = time.time()

    def update(self, error, error_derivative=None):
        """Update the PID controller
        Args:
            error (float): The current error
        """
        current_time = time.time()
        dt = current_time - self.last_time

        if dt == 0:
            return 0.0

        self.last_time = current_time

        self.integral = self._get_integral(error, dt)
        if error_derivative is None:
            derivative = self._get_derivative(error, dt)
        else:
            derivative = error_derivative

        # TODO: Calculate the PID output
        output = self._get_integral(error, dt) * self.K_i + self._get_derivative(error, dt) * self.K_d + self.K_p * error 

        self.last_error = error

        return output

    def _get_integral(self, error, dt):
        """Calculate the integral term
        Args:
            error (float): The current error
            dt (float): The time delta
        Returns:
            float: The integral term
        """

        # TODO: Calculate and return the integral term

        self.integral_error += error * dt

        return self.integral_error

    def _get_derivative(self, error, dt):
        """Calculate the derivative term
        Args:
            error (float): The current error
            dt (float): The time delta
        Returns:
            float: The derivative term
        """

        # TODO: Calculate and return the derivative term
        err_rate = (self.last_error - error) / dt
        return err_rate
