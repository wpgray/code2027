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

        # initiating the lift
        self.liftMotor = wpilib.Talon(8)
        self.liftMotor2 = wpilib.Talon(9)

        # Adjust the angle of the shooter
        self.shooterAngle = wpilib.Talon(10)


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

        # if button A is pushed, then Spin Shooter will take a ball in.
        if self.stick.getRawButton(1):
            self.leftSpinner.set(-1.0)
            self.rightSpinner.set(-1.0)
            self.loader.set(-1.0)
        elif self.stick.getRawButton(2):  # if button B is pushed, ball shoots out.
            self.leftSpinner.set(1.0)
            self.rightSpinner.set(1.0)
            self.loader.set(1.0)
        else:
            self.leftSpinner.set(0)
            self.rightSpinner.set(0)
            self.loader.set(0)

        # if Button X is pushed, then the elevator will go down
        if self.stick.getRawButton(3):
            self.liftMotor.set(-1.0)
            self.liftMotor2.set(-1.0)
        elif self.stick.getRawButton(4):  # if button Y is pushed, then the elevator will go up
            self.liftMotor.set(1.0)
            self.liftMotor2.set(1.0)
        else:
            self.liftMotor.set(0)
            self.liftMotor2.set(0)

        # if Left Bumper is pushed, then the shooter angle down
        if self.stick.getRawButton(5):
            self.shooterAngle.set(-1.0)
        elif self.stick.getRawButton(6):  # if right bumper pushed, shooter angle up
            self.shooterAngle.set(1.0)
        else:
            self.shooterAngle.set(0)

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()


if __name__ == "__main__":
    wpilib.run(MyRobot)
