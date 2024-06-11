# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       2602K KryptoKnights - 2023-2024                              #
# 	Created:      9/23/2023, 11:22:20 AM                                       #
# 	Description:  Robot Code for 2602K KryptoKnights                           #
#   Version:      V5.84                                                        #
#                                                                              #
# ---------------------------------------------------------------------------- #

from vex import *


brain=Brain()

FrontRight = Motor(Ports.PORT4, GearSetting.RATIO_6_1, True)
MiddleRight = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
BackRight = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
FrontLeft = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False)
MiddleLeft = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
BackLeft = Motor(Ports.PORT8, GearSetting.RATIO_6_1, False)
controller_1 = Controller(PRIMARY)
Catapult = Motor(Ports.PORT13, GearSetting.RATIO_36_1, True)
Catapult2 = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
Intake = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
FrontWingsPneumatic = DigitalOut(brain.three_wire_port.h)
inertial_gyro = Inertial(Ports.PORT20)
AutonSelector = Limit(brain.three_wire_port.e)
HangPneumatic = DigitalOut(brain.three_wire_port.c)
BackWingPneumaticR = DigitalOut(brain.three_wire_port.d)
BackWingPneumaticL = DigitalOut(brain.three_wire_port.g)
SideHangPneumatic = DigitalOut(brain.three_wire_port.f)

wait(230, MSEC)
print("\033[2J")
brain.screen.clear_screen()
controller_1.screen.clear_screen()

Deadband = 5
vexcode_brain_precision = 0
vexcode_console_precision = 0
WingsPressed = False
HangPressed = False
BackWingsPressed = False
SideHang = False
ForwardkP = 0.8
ForwardkI = 0.001
ForwardkD = 0.01
TurnkP = 2.4
TurnkI = 0.001
TurnkD = 0
error = 0
integral = 0
derivative = 0
preverror = 0
mmforward = 0
motorpower = 0
autonselect = 1

path = [(0, 0), (30, 10), (15, 15), (0, 0), (5, 7)]

def when_started1():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, autonselect
    FrontRight.set_stopping(COAST)
    MiddleRight.set_stopping(COAST)
    BackRight.set_stopping(COAST)
    FrontLeft.set_stopping(COAST)
    MiddleLeft.set_stopping(COAST)
    BackLeft.set_stopping(COAST)
    inertial_gyro.calibrate()
    while inertial_gyro.is_calibrating():
        sleep(50)
    Catapult.reset_position()
    autonselect = 0
    while FrontLeft.velocity(RPM) < 40:
        if AutonSelector.pressing():
            autonselect += 1
        if autonselect > 6:
            autonselect = 1
        if autonselect == 1:
            brain.screen.print("Autonomous Skills")
            controller_1.screen.print("Autonomous Skills")
        elif autonselect == 2:
            brain.screen.print("Defensive - 4 balls")
            controller_1.screen.print("Defensive - 4 balls")
        elif autonselect == 3:
            brain.screen.print("Defensive - 5 balls - S")
            controller_1.screen.print("Defensive - 5 balls - S")
        elif autonselect == 4:
            brain.screen.print("Defensive - 3 balls")
            controller_1.screen.print("Defensive - 3 balls")
        elif autonselect == 5:
            brain.screen.print("Offensive Side - 6 balls")
            controller_1.screen.print("Offensive Side - 6 balls")
        elif autonselect == 6:
            brain.screen.print("Offensive Side - 4 balls")
            controller_1.screen.print("Offensive Side - 4 balls")

        brain.screen.new_line()
        controller_1.screen.new_line()
        

def onauton_autonomous_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, error
    FrontRight.set_stopping(BRAKE)
    MiddleRight.set_stopping(BRAKE)
    BackRight.set_stopping(BRAKE)
    FrontLeft.set_stopping(BRAKE)
    MiddleLeft.set_stopping(BRAKE)
    BackLeft.set_stopping(BRAKE)
    goto()
    Turn_degrees2(angledegrees, 0)
    Forward_distance(distanceinches, 0)
    if autonselect == 1:
        #SKILLS - Autonomous 
        # starting position at the start        
        
        ##### CATAPULT #####
        #HangPneumatic.set(True)
        SideHangPneumatic.set(True)        
        Curve_distance(-32, 0, 12, 0.85)
        SideHangPneumatic.set(False)
        #HangPneumatic.set(False)
        Curve_distance(27, 0, -18, 0.85)
        Turn_degrees(87, 0)
        FrontWingsPneumatic.set(True)
        Catapult.set_velocity(63, RPM)
        Catapult2.set_velocity(63, RPM)
        Catapult.set_stopping(COAST)
        Catapult2.set_stopping(COAST)
        Catapult.spin(FORWARD)
        Catapult2.spin(FORWARD)
        wait(24, SECONDS)
        Catapult.stop()
        Catapult2.stop()
        FrontWingsPneumatic.set(False)
        Turn_degrees(138, 0)
        Curve_distance(-24, -11, 112, 0.81)
        Curve_distance(-54, 0, 112, 0.85)
        
        ##### RIGHT #####
        
        BackWingPneumaticR.set(True)
        Curve_distance(-68, -25, 22, 0.3)
        Curve_distance(10, 0, 27, 0.85)
        wait(300, MSEC)
        FrontRight.set_velocity(500, RPM)
        MiddleRight.set_velocity(500, RPM)
        BackRight.set_velocity(500, RPM)
        FrontLeft.set_velocity(500, RPM)
        MiddleLeft.set_velocity(500, RPM)
        BackLeft.set_velocity(500, RPM)
        FrontRight.spin(FORWARD)
        MiddleRight.spin(FORWARD)
        BackRight.spin(FORWARD)
        FrontLeft.spin(FORWARD)
        MiddleLeft.spin(FORWARD)
        BackLeft.spin(FORWARD)
        wait(0.5, SECONDS)
        FrontRight.stop()
        MiddleRight.stop()
        BackRight.stop()
        FrontLeft.stop()
        MiddleLeft.stop()
        BackLeft.stop()
        Curve_distance(9, 0, 32, 0.85)
        BackWingPneumaticR.set(False)

        ###### MIDDLE ######
        # Alignment for RIGHT side ---->
        Turn_degrees(-50, 0)
        Curve_distance(-50, 0, -50, 0.85)
        Turn_degrees(-103, 0)
        
        # Push from RIGHT side ---->
        FrontWingsPneumatic.set(True)
        Curve_distance(43, 0, -98, 0.85)
        FrontWingsPneumatic.set(False)
        Curve_distance(-20, 0, -68, 0.85)

        # Alignment for MIDDLE side --->
        Curve_distance(-25, 0, 22, 1.5)
        Turn_degrees(122, 0)
        
        # Push from MIDDLE side --->    
        BackWingPneumaticR.set(True)        
        BackWingPneumaticL.set(True)        
        FrontRight.set_velocity(500, RPM)
        MiddleRight.set_velocity(500, RPM)
        BackRight.set_velocity(500, RPM)
        FrontLeft.set_velocity(500, RPM)
        MiddleLeft.set_velocity(500, RPM)
        BackLeft.set_velocity(500, RPM)
        FrontRight.spin(FORWARD)
        MiddleRight.spin(FORWARD)
        BackRight.spin(FORWARD)
        FrontLeft.spin(FORWARD)
        MiddleLeft.spin(FORWARD)
        BackLeft.spin(FORWARD)
        wait(1, SECONDS)
        FrontRight.stop()
        MiddleRight.stop()
        BackRight.stop()
        FrontLeft.stop()
        MiddleLeft.stop()
        BackLeft.stop()
        Curve_distance(10, 0, 112, 0.85)
        Curve_distance(-12, 0, 112, 0.85)
        Curve_distance(35, 0, 112, 0.85)
        BackWingPneumaticR.set(False)        
        BackWingPneumaticL.set(False)
        
        # Alignment for LEFT side --->        
        Turn_degrees(202, 0)
        Curve_distance(35, 0, 202, 0.85)
        Turn_degrees(332, 0)
        
        # Push from LEFT side --->
        FrontWingsPneumatic.set(True)
        Curve_distance(43, 0, 332, 0.85)
        Curve_distance(-10, 0, -68, 0.85)
        
        Curve_distance(12, 0, -68, 0.85)
        FrontWingsPneumatic.set(False)
        Curve_distance(-10, 0, -68, 0.85)

        ##### LEFT #####
        
        Turn_degrees(-158, 0)
        Intake.set_velocity(180, RPM)
        Intake.spin(REVERSE)
        FrontWingsPneumatic.set(True)
        Curve_distance(38, 20, -83, 1.5)
        FrontWingsPneumatic.set(False)

        # Alignment for LEFT side ---->
        Turn_degrees(192, 0)
        Curve_distance(18, 0, 192, 0.85)
        Intake.stop()
        Turn_degrees(112, 0)
        
        # Push from LEFT side ---->
        BackWingPneumaticL.set(True)  
        Curve_distance(-45, -5, 182, 0.85)
        Curve_distance(18, 0, 177, 3.5)
        Curve_distance(-25, 0, 192, 2.5)
        Curve_distance(18, 0, 177, 3.5)
        Curve_distance(-25, 0, 192, 2.5)
        Curve_distance(9, 0, 187, 0.85)
        BackWingPneumaticL.set(False)

    elif autonselect == 2:
        #DEFENSIVE side Autonomous - MIDDLE BALL PICK
        
        SideHangPneumatic.set(True)
        FrontWingsPneumatic.set(True)
        Intake.set_velocity(180, RPM)
        Intake.spin(FORWARD)
        wait(300, MSEC)
        SideHangPneumatic.set(False)
        FrontWingsPneumatic.set(False) 
        Curve_distance(60, 0, 0, 0.85)
        #HangPneumatic.set(False)
        Intake.set_velocity(100, RPM)
        Curve_distance(-58, 0, 0, 0.85)
        Turn_degrees(115, 0)
        BackWingPneumaticL.set(True)       
        Curve_distance(-40, 0, 130, 0.85)
        Curve_distance(35, 0, 115, 0.85)
        BackWingPneumaticR.set(True)
        BackWingPneumaticL.set(False)
        Turn_degrees(0, 0)
        BackWingPneumaticR.set(False)
        Turn_degrees(90, 0)
        Intake.set_velocity(180, RPM)
        Intake.spin(REVERSE)
        Curve_distance(40, 0, 75, 1)
        wait(500, MSEC)
        Intake.stop()

    elif autonselect == 3:
        #DEFENSIVE side Autonomous - Elimination - 2 MIDDLE BALLS PICK
        
        SideHangPneumatic.set(True)
        FrontWingsPneumatic.set(True)
        Intake.set_velocity(180, RPM)
        Intake.spin(FORWARD)
        wait(300, MSEC)
        SideHangPneumatic.set(False)
        FrontWingsPneumatic.set(False) 
        Curve_distance(60, 0, 0, 0.85)
        Intake.set_velocity(100, RPM)
        Curve_distance(-5, 0, 0, 0.85)
        Turn_degrees(70, 0)
        FrontWingsPneumatic.set(True)
        Curve_distance(20, 0, 70, 0.85)
        FrontWingsPneumatic.set(False)
        Curve_distance(-20, 0, 70, 0.85)
        Curve_distance(-53, 0, 0, 0.85)
        Turn_degrees(115, 0)
        BackWingPneumaticL.set(True)       
        Curve_distance(-40, 0, 130, 0.85)
        Curve_distance(35, 0, 115, 0.85)
        BackWingPneumaticR.set(True)
        BackWingPneumaticL.set(False)
        Turn_degrees(0, 0)
        BackWingPneumaticR.set(False)
        Turn_degrees(90, 0)
        Intake.set_velocity(180, RPM)
        Intake.spin(REVERSE)
        Curve_distance(40, 0, 75, 1)
        wait(500, MSEC)
        Intake.stop()

    elif autonselect == 4:
        #DEFENSIVE side Autonomous - 3 balls pick (safe play)
        
        SideHangPneumatic.set(True)
        FrontWingsPneumatic.set(True)
        wait(300, MSEC)
        SideHangPneumatic.set(False)
        FrontWingsPneumatic.set(False)  
        Turn_degrees(115, 0)
        BackWingPneumaticL.set(True)        
        Forward_distance(-30, 0)
        Turn_degrees(140, 0)
        Forward_distance(-10, 0)
        Forward_distance(11, 0)
        BackWingPneumaticL.set(False)
        Turn_degrees(125, 0)
        Curve_distance(23, 0, 115, 0.85)
        BackWingPneumaticR.set(True)
        Turn_degrees(0, 0)
        BackWingPneumaticR.set(False)
        Turn_degrees(90, 0)
        Curve_distance(25, 0, 70, 0.85)
        Intake.set_velocity(180, RPM)
        Intake.spin(REVERSE)
        Forward_distance(17, 0)
        wait(500, MSEC)
        Intake.stop()
  
    elif autonselect == 5:
        #OFFENSIVE side Autonomous - 6 ball pick from hang side
        
        SideHangPneumatic.set(True)
        Intake.set_velocity(180, RPM)
        Intake.spin(FORWARD)
        wait(300, MSEC)
        SideHangPneumatic.set(False)
        Curve_distance(8, 0, 0, 0.85)
        Curve_distance(-8, 0, 0, 0.85)
        BackWingPneumaticL.set(True)
        BackWingPneumaticR.set(True)
        Curve_distance(-48, 0, -30, 0.85)
        Intake.stop()
        BackWingPneumaticL.set(False)
        Curve_distance(-23, 0, -80, 1.5)
        Curve_distance(15, 0, -60, 1.5)
        BackWingPneumaticR.set(False)
        Intake.set_velocity(180, RPM)
        Intake.spin(REVERSE)
        Curve_distance(16, 0, 90, 0.85)
        Curve_distance(-10, 0, 90, 0.85)
        Intake.stop()
        BackWingPneumaticR.set(False)
        Intake.set_velocity(120, RPM)
        Intake.spin(FORWARD)
        Curve_distance(54, 0, 20, 0.85)
        Turn_degrees(145, 10)
        Intake.set_velocity(180, RPM)
        Intake.spin(REVERSE)
        Curve_distance(10, 0, 145, 0.85)
        wait(250, MSEC)
        Intake.set_velocity(180, RPM)
        Intake.spin(FORWARD)
        Curve_distance(22, 0, 45, 0.85)
        Turn_degrees(180, 10)
        Intake.spin(REVERSE)
        FrontWingsPneumatic.set(True)
        Curve_distance(37, 0, 180, 0.85)
        FrontWingsPneumatic.set(False)
        Curve_distance(-10, 0, 180, 0.85)
        Intake.stop()

    elif autonselect == 6:
        #OFFENSIVE side Autonomous - 4 ball pick from hang side
    
        SideHangPneumatic.set(True)
        Intake.set_velocity(180, RPM)
        Intake.spin(FORWARD)
        wait(300, MSEC)
        SideHangPneumatic.set(False)
        Curve_distance(8, 0, 0, 0.85)
        Curve_distance(-8, 0, 0, 0.85)
        BackWingPneumaticL.set(True)
        BackWingPneumaticR.set(True)
        Curve_distance(-48, 0, -30, 0.85)
        Intake.stop()
        BackWingPneumaticL.set(False)
        Curve_distance(-23, 0, -80, 1.5)
        Curve_distance(15, 0, -60, 1.5)
        BackWingPneumaticR.set(False)
        Intake.set_velocity(180, RPM)
        Intake.spin(REVERSE)
        Curve_distance(16, 0, 90, 0.85)
        Curve_distance(-10, 0, 90, 0.85)
        Intake.stop()
        BackWingPneumaticR.set(False)
        Intake.set_velocity(120, RPM)
        Intake.spin(FORWARD)
        Curve_distance(54, 0, 20, 0.85)
        Turn_degrees(145, 10)
        Intake.set_velocity(180, RPM)
        Intake.spin(REVERSE)
        Curve_distance(41, 0, 145, 0.85)
        Curve_distance(-10, 0, 180, 0.85)
        Intake.stop()


def ondriver_drivercontrol_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    FrontWingsPneumatic.set(False)
    BackWingPneumaticL.set(False)
    BackWingPneumaticR.set(False)
    SideHangPneumatic.set(False)
    FrontRight.set_stopping(COAST)
    MiddleRight.set_stopping(COAST)
    BackRight.set_stopping(COAST)
    FrontLeft.set_stopping(COAST)
    MiddleLeft.set_stopping(COAST)
    BackLeft.set_stopping(COAST)
    while True:
        if math.fabs(controller_1.axis1.position()) + math.fabs(controller_1.axis3.position()) > Deadband:
            if math.fabs(controller_1.axis1.position()) > -360 and math.fabs(controller_1.axis1.position()) < 360:
                #turning
                FrontRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                MiddleRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                BackRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                FrontLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
                MiddleLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
                BackLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
            elif math.fabs(controller_1.axis3.position()) > 0 and math.fabs(controller_1.axis3.position()) < 180:
                #forward
                FrontRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                MiddleRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                BackRight.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()) + 10, PERCENT)
                FrontLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
                MiddleLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)
                BackLeft.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()) + 10, PERCENT)  
        else:
            FrontRight.set_velocity(0, RPM)
            MiddleRight.set_velocity(0, RPM)
            BackRight.set_velocity(0, RPM)
            FrontLeft.set_velocity(0, RPM)
            MiddleLeft.set_velocity(0, RPM)
            BackLeft.set_velocity(0, RPM)
        FrontRight.spin(REVERSE)
        MiddleRight.spin(REVERSE)
        BackRight.spin(REVERSE)
        FrontLeft.spin(REVERSE)
        MiddleLeft.spin(REVERSE)
        BackLeft.spin(REVERSE)
        wait(10, MSEC)
        
def Forward_distance(Forward_distance__distance, Forward_distance__speed):
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed, ForwardkP, ForwardkI, ForwardkD, TurnkP, TurnkI, TurnkD, error, integral, derivative, preverror, mmforward, motorpower
    error = 0
    integral = 0
    derivative = 0
    preverror = 0
    motorpower = 0
    FrontLeft.set_position(0, DEGREES)
    FrontRight.set_position(0, DEGREES)
    MiddleLeft.set_position(0, DEGREES)
    MiddleRight.set_position(0, DEGREES)
    BackLeft.set_position(0, DEGREES)
    BackRight.set_position(0, DEGREES)
    mmforward = ((Forward_distance__distance * 25.4) * 2)
    inertial_gyro.reset_rotation()
    error = mmforward - (0 -((((FrontLeft.position(DEGREES) + MiddleLeft.position(DEGREES) + BackLeft.position(DEGREES)) / 3) + (FrontRight.position(DEGREES) + MiddleRight.position(DEGREES) + BackRight.position(DEGREES)) / 3)) / 2)
    while not abs(error) < 5:
        error = mmforward - (0 -((((FrontLeft.position(DEGREES) + MiddleLeft.position(DEGREES) + BackLeft.position(DEGREES)) / 3) + (FrontRight.position(DEGREES) + MiddleRight.position(DEGREES) + BackRight.position(DEGREES)) / 3)) / 2)
        derivative = error - preverror
        preverror = error
        motorpower = (ForwardkP * error + ForwardkI * integral) + ForwardkD * derivative
        if motorpower > 400:
            motorpower = 400
        elif motorpower < -400:
            motorpower = -400
        FrontRight.set_velocity(motorpower+(0-inertial_gyro.rotation()) + Forward_distance__speed, RPM)
        MiddleRight.set_velocity(motorpower+(0-inertial_gyro.rotation()) + Forward_distance__speed, RPM)
        BackRight.set_velocity(motorpower+(0-inertial_gyro.rotation()) + Forward_distance__speed, RPM)
        FrontLeft.set_velocity(motorpower-(0-inertial_gyro.rotation()) + Forward_distance__speed, RPM)
        MiddleLeft.set_velocity(motorpower-(0-inertial_gyro.rotation()) + Forward_distance__speed, RPM)
        BackLeft.set_velocity(motorpower-(0-inertial_gyro.rotation()) + Forward_distance__speed, RPM)
        FrontRight.spin(REVERSE)
        MiddleRight.spin(REVERSE)
        BackRight.spin(REVERSE)
        FrontLeft.spin(REVERSE)
        MiddleLeft.spin(REVERSE)
        BackLeft.spin(REVERSE)
        wait(20, MSEC)
    FrontRight.stop()
    MiddleRight.stop()
    BackRight.stop()
    FrontLeft.stop()
    MiddleLeft.stop()
    BackLeft.stop()
    motorpower = 0
    
def Turn_degrees(Turn_degrees__degrees, Turn_degrees__speed):
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed, ForwardkP, ForwardkI, ForwardkD, TurnkP, TurnkI, TurnkD, error, integral, derivative, preverror, mmforward, motorpower
    error = 0
    integral = 0
    derivative = 0
    preverror = 0
    motorpower = 0
    error = ((Turn_degrees__degrees - inertial_gyro.heading(DEGREES) + 180) % 360) - 180
    brain.timer.clear()
    while not abs(error) < 1:
        error = ((Turn_degrees__degrees - inertial_gyro.heading(DEGREES) + 180) % 360) - 180
        integral += error
        derivative = (error - preverror)
        preverror = error
        motorpower = (TurnkP * error + TurnkI * integral) + TurnkD * derivative
        if motorpower > 400:
            motorpower = 400
        elif motorpower < -400:
            motorpower = -400
        FrontRight.set_velocity(motorpower + Turn_degrees__speed, RPM)
        MiddleRight.set_velocity(motorpower + Turn_degrees__speed, RPM)
        BackRight.set_velocity(motorpower + Turn_degrees__speed, RPM)
        FrontLeft.set_velocity(motorpower + Turn_degrees__speed, RPM)
        MiddleLeft.set_velocity(motorpower + Turn_degrees__speed, RPM)
        BackLeft.set_velocity(motorpower + Turn_degrees__speed, RPM)
        FrontRight.spin(FORWARD)
        MiddleRight.spin(FORWARD)
        BackRight.spin(FORWARD)
        FrontLeft.spin(REVERSE)
        MiddleLeft.spin(REVERSE)
        BackLeft.spin(REVERSE)
        print(error)
        wait(20, MSEC)
    FrontRight.stop()
    MiddleRight.stop()
    BackRight.stop()
    FrontLeft.stop()
    MiddleLeft.stop()
    BackLeft.stop()
    motorpower = 0
    
def Turn_degrees2(Turn_degrees2__degrees, Turn_degrees2__speed):
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed, ForwardkP, ForwardkI, ForwardkD, TurnkP, TurnkI, TurnkD, error, integral, derivative, preverror, mmforward, motorpower
    error = 0
    integral = 0
    derivative = 0
    preverror = 0
    motorpower = 0
    inertial_gyro.reset_rotation()
    error = Turn_degrees2__degrees - inertial_gyro.rotation(DEGREES)
    brain.timer.clear()
    while not abs(error) < 1:
        error = Turn_degrees2__degrees - inertial_gyro.rotation(DEGREES)
        integral += error
        derivative = (error - preverror)
        preverror = error
        motorpower = (TurnkP * error + TurnkI * integral) + TurnkD * derivative
        if motorpower > 400:
            motorpower = 400
        elif motorpower < -400:
            motorpower = -400
        FrontRight.set_velocity(motorpower + Turn_degrees2__speed, RPM)
        MiddleRight.set_velocity(motorpower + Turn_degrees2__speed, RPM)
        BackRight.set_velocity(motorpower + Turn_degrees2__speed, RPM)
        FrontLeft.set_velocity(motorpower + Turn_degrees2__speed, RPM)
        MiddleLeft.set_velocity(motorpower + Turn_degrees2__speed, RPM)
        BackLeft.set_velocity(motorpower + Turn_degrees2__speed, RPM)
        FrontRight.spin(FORWARD)
        MiddleRight.spin(FORWARD)
        BackRight.spin(FORWARD)
        FrontLeft.spin(REVERSE)
        MiddleLeft.spin(REVERSE)
        BackLeft.spin(REVERSE)
        print(error)
        wait(20, MSEC)
    FrontRight.stop()
    MiddleRight.stop()
    BackRight.stop()
    FrontLeft.stop()
    MiddleLeft.stop()
    BackLeft.stop()
    motorpower = 0
    
def Curve_distance(Curve_distance__distance, Curve_distance__distance_before_turn, Curve_distance__degrees, Curve_distance__correction_strength):
    global ForwardkP, ForwardkI, ForwardkD, TurnkP, TurnkI, TurnkD, error, integral, derivative, preverror, mmforward, motorpower, vexcode_brain_precision, vexcode_console_precision
    errorDrive = 0
    integralDrive = 0
    derivativeDrive = 0
    preverrorDrive = 0
    errorAngle = 0
    integralAngle = 0
    derivativeAngle = 0
    preverrorAngle = 0
    motorpowerDrive = 0
    motorpowerAngle = 0
    FrontLeft.set_position(0, DEGREES)
    FrontRight.set_position(0, DEGREES)
    MiddleLeft.set_position(0, DEGREES)
    MiddleRight.set_position(0, DEGREES)
    BackLeft.set_position(0, DEGREES)
    BackRight.set_position(0, DEGREES)
    inertial_gyro.reset_rotation()
    mmforward = (Curve_distance__distance * 25.4) * 2
    errorDrive = mmforward - (0 - ((((FrontLeft.position(DEGREES) + MiddleLeft.position(DEGREES) + BackLeft.position(DEGREES)) / 3) + (FrontRight.position(DEGREES) + MiddleRight.position(DEGREES) + BackRight.position(DEGREES)) / 3)) / 2)
    errorAngle = Curve_distance__degrees - inertial_gyro.rotation(DEGREES)
    brain.timer.clear()
    while not (abs(errorDrive) < 5 and abs(errorAngle) < 1):
        errorDrive = mmforward - (0 - ((((FrontLeft.position(DEGREES) + MiddleLeft.position(DEGREES) + BackLeft.position(DEGREES)) / 3) + (FrontRight.position(DEGREES) + MiddleRight.position(DEGREES) + BackRight.position(DEGREES)) / 3)) / 2)
        integralDrive += errorDrive
        derivativeDrive = errorDrive - preverrorDrive
        preverrorDrive = errorDrive
        motorpowerDrive = ((ForwardkP * errorDrive + ForwardkI * integralDrive) + ForwardkD * derivativeDrive)
        errorAngle = Curve_distance__degrees - inertial_gyro.rotation(DEGREES)
        integralAngle += errorAngle
        derivativeAngle = errorAngle - preverrorAngle
        preverrorAngle = errorAngle
        if abs((((((FrontLeft.position(DEGREES) + MiddleLeft.position(DEGREES) + BackLeft.position(DEGREES)) / 3) + (FrontRight.position(DEGREES) + MiddleRight.position(DEGREES) + BackRight.position(DEGREES)) / 3)) / 2) * 0.0393701) < Curve_distance__distance_before_turn:
            angleOutput = 0
        else:
            angleOutput = 1
        motorpowerAngle = ((TurnkP * errorAngle + TurnkI * integralAngle) + TurnkD * derivativeAngle) * Curve_distance__correction_strength * angleOutput
        if abs(errorAngle) < 1:
            angleOutput = 0
        if motorpowerDrive > 400:
            motorpowerDrive = 400
        elif motorpowerDrive < -400:
            motorpowerDrive = -400
        if motorpowerAngle > 400:
            motorpowerAngle = 400
        elif motorpowerAngle < -400:
            motorpowerAngle = -400
        if motorpowerDrive > 0 and motorpowerDrive < 30:
            break
        elif motorpowerDrive < 0 and motorpowerDrive > -30:
            break
        FrontRight.set_velocity(motorpowerDrive - motorpowerAngle, RPM)
        MiddleRight.set_velocity(motorpowerDrive - motorpowerAngle, RPM)
        BackRight.set_velocity(motorpowerDrive - motorpowerAngle, RPM)
        FrontLeft.set_velocity(motorpowerDrive + motorpowerAngle, RPM)
        MiddleLeft.set_velocity(motorpowerDrive + motorpowerAngle, RPM)
        BackLeft.set_velocity(motorpowerDrive + motorpowerAngle, RPM)
        FrontRight.spin(REVERSE)
        MiddleRight.spin(REVERSE)
        BackRight.spin(REVERSE)
        FrontLeft.spin(REVERSE)
        MiddleLeft.spin(REVERSE)
        BackLeft.spin(REVERSE)
        wait(20, MSEC)
    FrontRight.stop()
    MiddleRight.stop()
    BackRight.stop()
    FrontLeft.stop()
    MiddleLeft.stop()
    BackLeft.stop()
    motorpower = 0
    
def goto():
    global angledegrees, distanceinches
    for point1 in path[0:1]:
        pass
    for point2 in path[1:2]:
        path.pop(0)
    distanceinches = (((point2[0] - point1[0])**2) + ((point2[1] - point1[1])**2))**0.5
    oppositeside = point2[1] - point1[1]
    angledegrees = oppositeside/distanceinches*(180/math.pi) - 90
    
def odomprog():
    xlocation = ((((((((FrontLeft.position(DEGREES) + MiddleLeft.position(DEGREES) + BackLeft.position(DEGREES)) / 3) + (FrontRight.position(DEGREES) + MiddleRight.position(DEGREES) + BackRight.position(DEGREES)) / 3)) / 2) * 0.0393701)) * (5/3)) * math.cos(inertial_gyro.heading())
    
def onevent_controller_1buttonL2_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    #wings out/in
    if WingsPressed == True:
        FrontWingsPneumatic.set(False)
        WingsPressed = False
    else:
        FrontWingsPneumatic.set(True)
        WingsPressed = True

def onevent_controller_1buttonR2_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed, BackWingsPressed
    #wings out/in
    if BackWingsPressed == True:
        BackWingPneumaticR.set(False)
        BackWingPneumaticL.set(False)
        BackWingsPressed = False
    else:
        BackWingPneumaticR.set(True)
        BackWingPneumaticL.set(True)
        BackWingsPressed = True

def onevent_controller_1buttonR1_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    #matchload
    Catapult.set_velocity(63, RPM)
    Catapult2.set_velocity(63, RPM)
    Catapult.set_stopping(COAST)
    Catapult2.set_stopping(COAST)
    Catapult.spin(FORWARD)
    Catapult2.spin(FORWARD)
    while controller_1.buttonR1.pressing():
        wait(5, MSEC)
    while not controller_1.buttonR1.pressing():
        wait(5, MSEC)
    Catapult.stop()
    Catapult2.stop()
    wait(200, MSEC)
    
def onevent_controller_1buttonL1_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    #outake
    Intake.stop()
    Intake.set_velocity(180, RPM)
    Intake.spin(REVERSE)
    while controller_1.buttonL1.pressing():
        wait(5, MSEC)
    Intake.stop()

def onevent_controller_1buttonY_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed
    #intake
    Intake.set_stopping(COAST)
    Intake.set_velocity(180, RPM)
    Intake.spin(FORWARD)
    while not controller_1.buttonL1.pressing():
        wait(5, MSEC)
    Intake.stop()
    
def onevent_controller_1buttonRight_pressed_0():
    global Deadband, vexcode_brain_precision, vexcode_console_precision, WingsPressed, HangPressed
    brain.timer.clear()
    #hang up/down
    if HangPressed == True:
        HangPneumatic.set(False)
        HangPressed = False
    else:
        HangPneumatic.set(True)
        HangPressed = True
        
def onevent_controller_1buttonLeft_pressed_0():
    global SideHang
    if SideHang == True:
       SideHangPneumatic.set(False)
       SideHang = False
    else:
       SideHangPneumatic.set(True)
       SideHang = True

def vexcode_auton_function():
    global runodom
    auton_task_0 = Thread(onauton_autonomous_0)
    runodom = Thread(odomprog)
    while(competition.is_autonomous() and competition.is_enabled()):
        wait(10, MSEC)
    auton_task_0.stop()

def vexcode_driver_function():
    driver_control_task_0 = Thread(ondriver_drivercontrol_0)
    while(competition.is_driver_control() and competition.is_enabled()):
        wait(10, MSEC)
    driver_control_task_0.stop()

competition = Competition(vexcode_driver_function, vexcode_auton_function)
controller_1.buttonL2.pressed(onevent_controller_1buttonL2_pressed_0)
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonY.pressed(onevent_controller_1buttonY_pressed_0)
controller_1.buttonRight.pressed(onevent_controller_1buttonRight_pressed_0)
controller_1.buttonR2.pressed(onevent_controller_1buttonR2_pressed_0)
controller_1.buttonLeft.pressed(onevent_controller_1buttonLeft_pressed_0)
when_started1()