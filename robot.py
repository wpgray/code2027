"""
    This is a good foundation to build your robot code on
"""

import wpilib


class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        # Initiates the robot drive and joystiq
        self.robot_drive = wpilib.RobotDrive(0, 1, 2, 3)
        self.stick = wpilib.Joystick(0)

        # Initiates Ball shooter
        self.leftSpinner = wpilib.Talon(4)
        self.rightSpinner = wpilib.Talon(5)

        # Iniates Aimer motor and Loader
        self.aimer = wpilib.Talon(6)
        self.loader = wpilib.Talon(7)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Check if we've completed 100 loops (approximately 2 seconds)
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(-0.5, 0)  # Drive forwards at half speed
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.robot_drive.arcadeDrive(self.stick)

        # if button A is pushed, Spin Shooter so it can take a ball in.
        if self.stick.getRawButton(1):
            self.leftSpinner.set(-1.0)
            self.rightSpinner.set(-1.0)
        else:
            self.leftSpinner.set(0)
            self.rightSpinner.set(0)

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()


if __name__ == "__main__":
    wpilib.run(MyRobot)
