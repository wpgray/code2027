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

        # Initiates the robot drive and joystick
        self.leftWheels = wpilib.Talon(0)
        self.rightWheels = wpilib.Talon(1)
        self.leftWheels.setInverted(True)
        self.robot_drive = wpilib.RobotDrive(self.leftWheels, self.rightWheels)
        self.stick = wpilib.Joystick(0)
        self.stick1 = wpilib.Joystick(1)

        # initiates servos
        self.servo = wpilib.Servo(2)
        self.servo1 = wpilib.Servo(3)

        # Initiates Ball shooter
        self.leftSpinner = wpilib.Talon(4)
        self.rightSpinner = wpilib.Talon(5)

        # Initiates angle motor and Loader
        self.aimer = wpilib.Talon(6)
        self.loader = wpilib.Talon(7)

        # Initiating the lift
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
        """
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(-0.5, 0)  # Drive forwards at half speed
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)  # Stop robot
        """

        # go forward and drive/ this was commented out due to being a mock-up
        if self.auto_loop_counter < 100:  # two seconds
            self.robot_drive.drive(-0.5, 0)
            self.leftSpinner.set(1.0)
            self.rightSpinner.set(1.0)
            self.loader.set(1.0)
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)
            self.loader.set(0.0)
            self.leftSpinner.set(0.0)
            self.rightSpinner.set(0.0)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.robot_drive
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

        # if Button X is pushed, then the elevator will go down(controller 2)
        if self.stick1.getRawButton(3):
            self.liftMotor.set(-1.0)
            self.liftMotor2.set(-1.0)
        elif self.stick1.getRawButton(4):  # if button Y is pushed, then the elevator will go up
            self.liftMotor.set(1.0)
            self.liftMotor2.set(1.0)
        else:
            self.liftMotor.set(0)
            self.liftMotor2.set(0)

        # if Left Bumper is pushed, then the shooter angle lessens
        if self.stick.getRawButton(5):
            self.shooterAngle.set(-1.0)
        elif self.stick.getRawButton(6):  # if right bumper pushed, shooter angle up
            self.shooterAngle.set(1.0)
        else:
            self.shooterAngle.set(0)

        # Camera servo control, needs testing
        if self.stick1.getRawButton(5):
            self.servo.set(0.0)
        elif self.stick1.getRawButton(6):
            self.servo.set(1.0)



    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()


if __name__ == "__main__":
    wpilib.run(MyRobot)
