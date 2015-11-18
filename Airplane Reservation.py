import os
import time


class DictonaryAirplaneSeats:
    def __init__(self):
        self.leftSeat = {}
        self.rightSeat = {}


class AirplaneSeats:

    def __init__(self):
        self.leftSeatNumber = ['L00', 'L01', 'L02', 'L03', 'L04', 'L05', 'L06', 'L07', 'L08', 'L09']
        self.leftSeatStatus = ['vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant']
        self.rightSeatNumber = ['R00', 'R01', 'R02', 'R03', 'R04', 'R05', 'R06', 'R07', 'R08', 'R09']
        self.rightSeatStatus = ['vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant', 'vacant']
        self.menuHolder = ''

    def reserve_seat(self):
        os.system('cls')
        print "<<<Seat Reservation>>>"
        reserved_seat = raw_input("Enter Seat Number: ")

        if reserved_seat == 'L00':
            if self.leftSeatStatus[0] == 'vacant':
                self.leftSeatStatus[0] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[0] == 'Reserved':
                print "L00 is already Reserved. Choose another one"
                print "Program restarting in 5 seconds"
                time.sleep(5)
                self.reserve_seat()
        elif reserved_seat == 'L01':
            if self.leftSeatStatus[1] == 'vacant':
                self.leftSeatStatus[1] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[1] == 'Reserved':
                print "L01 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'L02':
            if self.leftSeatStatus[2] == 'vacant':
                self.leftSeatStatus[2] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[2] == 'Reserved':
                print "L02 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'L03':
            if self.leftSeatStatus[2] == 'vacant':
                self.leftSeatStatus[2] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[2] == 'Reserved':
                print "L02 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'L04':
            if self.leftSeatStatus[4] == 'vacant':
                self.leftSeatStatus[4] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[4] == 'Reserved':
                print "L04 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'L05':
            if self.leftSeatStatus[5] == 'vacant':
                self.leftSeatStatus[5] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[5] == 'Reserved':
                print "L05 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'L06':
            if self.leftSeatStatus[6] == 'vacant':
                self.leftSeatStatus[6] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[6] == 'Reserved':
                print "L06 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'L07':
            if self.leftSeatStatus[7] == 'vacant':
                self.leftSeatStatus[7] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[7] == 'Reserved':
                print "L07 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'L08':
            if self.leftSeatStatus[8] == 'vacant':
                self.leftSeatStatus[8] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[8] == 'Reserved':
                print "L08 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'L09':
            if self.leftSeatStatus[9] == 'vacant':
                self.leftSeatStatus[9] = 'Reserved'
                self.restart_program()
            elif self.leftSeatStatus[9] == 'Reserved':
                print "L09 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R00':
            if self.rightSeatStatus[0] == 'vacant':
                self.rightSeatStatus[0] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[0] == 'Reserved':
                print "R00 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R01':
            if self.rightSeatStatus[1] == 'vacant':
                self.rightSeatStatus[1] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[1] == 'Reserved':
                print "R01 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R02':
            if self.rightSeatStatus[2] == 'vacant':
                self.rightSeatStatus[2] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[2] == 'Reserved':
                print "R02 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R03':
            if self.rightSeatStatus[3] == 'vacant':
                self.rightSeatStatus[3] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[3] == 'Reserved':
                print "R03 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R04':
            if self.rightSeatStatus[4] == 'vacant':
                self.rightSeatStatus[4] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[4] == 'Reserved':
                print "R04 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R05':
            if self.rightSeatStatus[5] == 'vacant':
                self.rightSeatStatus[5] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[5] == 'Reserved':
                print "R05 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R06':
            if self.rightSeatStatus[6] == 'vacant':
                self.rightSeatStatus[6] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[6] == 'Reserved':
                print "R06 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R07':
            if self.rightSeatStatus[7] == 'vacant':
                self.rightSeatStatus[7] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[7] == 'Reserved':
                print "R07 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R08':
            if self.rightSeatStatus[8] == 'vacant':
                self.rightSeatStatus[8] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[8] == 'Reserved':
                print "R08 is already Reserved. Choose another one"
                self.reserve_seat()
        elif reserved_seat == 'R09':
            if self.rightSeatStatus[9] == 'vacant':
                self.rightSeatStatus[9] = 'Reserved'
                self.restart_program()
            elif self.rightSeatStatus[9] == 'Reserved':
                print "R09 is already Reserved. Choose another one"
                self.reserve_seat()
        else:
            print "The seat you chose is not on this plane"
            print "Program will restart in 5 seconds"
            x = 5
            while x != 0:
                print str(x)
                time.sleep(1)
                x -= 1
            self.reserve_seat()
        #print "\n\nSeat Number "+str()

    def modify_seat(self):
        os.system('cls')
        print "<<<Change Reserved Seat(s)>>>\n"
        original_seat = raw_input("From Seat Number: ")
        if original_seat in self.leftSeatNumber or original_seat in self.rightSeatNumber:
            original_seat_list = list(original_seat)
            if original_seat_list[0] == 'L':
                if self.leftSeatStatus[int(original_seat_list[-1])] == 'Reserved':
                    new_seat = raw_input("To Seat Number: ")
                    new_seat_list = list(new_seat)
                    if new_seat_list[0] == 'L':
                        if self.leftSeatStatus[int(new_seat_list[-1])] == 'vacant':
                            self.leftSeatStatus[int(original_seat_list[-1])] = 'vacant'
                            self.leftSeatStatus[int(new_seat_list[-1])] = 'Reserved'
                            print "Seat Number " + str(self.leftSeatNumber[int(original_seat_list[-1])]) + " is now " + str(self.leftSeatStatus[int(original_seat_list[-1])])
                            print "Reserved seat has been transferred to "+str(self.leftSeatNumber[int(new_seat_list[-1])])+" which is now "+str(self.leftSeatStatus[int(new_seat_list[-1])]), "\n"
                            print "<<<Seats has been processed>>>"
                            raw_input("<Press Enter to continue>")
                            self.restart_program()
                        elif self.leftSeatStatus[int(new_seat_list[-1])] == 'Reserved':
                            print "The seat is already reserved"
                            print "Program will restart in 5 seconds"
                            x = 5
                            while x != 0:
                                print str(x)
                                time.sleep(1)
                                x -= 1
                            self.modify_seat()
                    elif new_seat_list[0] == 'R':
                        if self.rightSeatStatus[int(new_seat_list[-1])] == 'vacant':
                            self.leftSeatStatus[int(original_seat_list[-1])] = 'vacant'
                            self.rightSeatStatus[int(new_seat_list[-1])] = 'Reserved'
                            print "Seat Number " + str(self.leftSeatNumber[int(original_seat_list[-1])]) + " is now " + str(self.leftSeatStatus[int(original_seat_list[-1])])
                            print "Reserved seat has been transferred to "+str(self.rightSeatNumber[int(new_seat_list[-1])])+" which is now "+str(self.rightSeatStatus[int(new_seat_list[-1])]), "\n"
                            print "<<<Seats has been processed>>>"
                            raw_input("<Press Enter to continue>")
                            self.restart_program()
                        elif self.rightSeatStatus[int(new_seat_list[-1])] == 'Reserved':
                            print "The seat is already reserved"
                            print "Program will restart in 5 seconds"
                            x = 5
                            while x != 0:
                                print str(x)
                                time.sleep(1)
                                x -= 1
                            self.modify_seat()
                elif self.leftSeatStatus[int(original_seat_list[-1])] == 'vacant':
                    print "No one is occupying the seat"
                    raw_input("<Press Enter to Restart Program>>")
                    self.modify_seat()

            elif original_seat_list[0] == 'R':
                if self.rightSeatStatus[int(original_seat_list[-1])] == 'Reserved':
                    new_seat = raw_input("To Seat Number: ")
                    new_seat_list = list(new_seat)

                    if new_seat_list[0] == 'L':
                        if self.leftSeatStatus[int(new_seat_list[-1])] == 'vacant':
                            self.rightSeatStatus[int(original_seat_list[-1])] = 'vacant'
                            self.leftSeatStatus[int(new_seat_list[-1])] = 'Reserved'
                            print "Seat Number " + str(self.rightSeatNumber[int(original_seat_list[-1])]) + " is now " + str(self.rightSeatStatus[int(original_seat_list[-1])])
                            print "Reserved seat has been transferred to "+str(self.leftSeatNumber[int(new_seat_list[-1])])+" which is now "+str(self.leftSeatStatus[int(new_seat_list[-1])]), "\n"
                            print "<<<Seats has been processed>>>"
                            raw_input("<Press Enter to continue>")
                            self.restart_program()
                        elif self.leftSeatStatus[int(new_seat_list[-1])] == 'Reserved':
                            print "The seat is already reserved"
                            print "Program will restart in 5 seconds"
                            x = 5
                            while x != 0:
                                print str(x)
                                time.sleep(1)
                                x -= 1
                            self.modify_seat()
                    elif new_seat_list[0] == 'R':
                        if self.rightSeatStatus[int(new_seat_list[-1])] == 'vacant':
                            self.rightSeatStatus[int(original_seat_list[-1])] = 'vacant'
                            self.rightSeatStatus[int(new_seat_list[-1])] = 'Reserved'
                            print "Seat Number " + str(self.rightSeatNumber[int(original_seat_list[-1])]) + " is now " + str(self.rightSeatStatus[int(original_seat_list[-1])])
                            print "Reserved seat has been transferred to "+str(self.rightSeatNumber[int(new_seat_list[-1])])+" which is now "+str(self.rightSeatStatus[int(new_seat_list[-1])]), "\n"
                            print "<<<Seats has been processed>>>"
                            raw_input("<Press Enter to continue>")
                            self.restart_program()
                        elif self.rightSeatStatus[int(new_seat_list[-1])] == 'Reserved':
                            print "The seat is already reserved"
                            print "Program will restart in 5 seconds"
                            x = 5
                            while x != 0:
                                print str(x)
                                time.sleep(1)
                                x -= 1
                            self.modify_seat()
                    elif self.rightSeatStatus[int(new_seat_list[-1])] == 'Reserved':
                        print "The seat is already reserved"
                        raw_input("<Press Enter>")
                        self.modify_seat()
                elif self.leftSeatStatus[int(original_seat_list[-1])] == 'vacant':
                    print "No one is occupying the seat"
                    raw_input("<Press Enter to Restart Program>>")
                    self.modify_seat()
        elif original_seat not in self.leftSeatNumber and original_seat not in self.rightSeatNumber:
            print "Original Seat Number is not on this plane"
            print "Program will restart in 5 seconds!"
            x = 5
            while x != 0:
                print str(x)
                time.sleep(1)
                x -= 1
            self.modify_seat()

    def cancel_seat(self):
        os.system('cls')
        print "<<<Cancel Reserved Seat>>>\n"
        seat_to_cancel = raw_input("Enter seat to cancel: ")
        seat_to_cancel_list = list(seat_to_cancel)
        if seat_to_cancel_list[0] == 'L':
            if self.leftSeatStatus[int(seat_to_cancel_list[-1])] == 'Reserved':
                self.leftSeatStatus[int(seat_to_cancel_list[-1])] = 'vacant'
                print "\nSeat Number " + str(self.leftSeatNumber[int(seat_to_cancel_list[-1])]) + " is now " + str(self.leftSeatStatus[int(seat_to_cancel_list[-1])])
                self.restart_program()
            elif self.leftSeatStatus[int(seat_to_cancel_list[-1])] == 'vacant':
                print "\nThe Seat Number " + str(self.leftSeatNumber[int(seat_to_cancel_list[-1])]) + " is currently " + str(self.leftSeatStatus[int(seat_to_cancel_list[-1])])
                print "Program will now restart in 5 seconds"
                x = 5
                while x != 0:
                    print str(x)
                    time.sleep(1)
                    x -= 1
                self.cancel_seat()
        elif seat_to_cancel_list[0] == 'R':
            if self.rightSeatStatus[int(seat_to_cancel_list[-1])] == 'Reserved':
                self.rightSeatStatus[int(seat_to_cancel_list[-1])] = 'vacant'
                print "\nThe Seat Number " + str(self.rightSeatNumber[int(seat_to_cancel_list[-1])]) + " is now " + str(self.rightSeatStatus[int(seat_to_cancel_list[-1])])
                self.restart_program()
            elif self.rightSeatStatus[int(seat_to_cancel_list[-1])] == 'vacant':
                print "\nThe Seat Number " + str(self.rightSeatNumber[int(seat_to_cancel_list[-1])]) + " is currently " + str(self.rightSeatStatus[int(seat_to_cancel_list[-1])])
                print "Program will now restart in 5 seconds"
                x = 5
                while x != 0:
                    print str(x)
                    time.sleep(1)
                    x -= 1
                self.cancel_seat()
    def display_seat_chart(self):
        os.system('cls')
        x = len(self.leftSeatNumber)
        y = len(self.rightSeatNumber)
        for i in range(0, int(x), 1):
            print str(self.leftSeatNumber[i]), "      ", str(self.leftSeatStatus[i]),"      ",str(self.rightSeatNumber[i]), "      ",str(self.rightSeatStatus[i])
        raw_input("<Press Enter to continue>")
        self.restart_program()
    def restart_program(self):
        os.system('cls')
        if self.menuHolder.lower() == 'a':
            print """
    A. RESERVE another seat
    B. Go to MAIN MENU
            """
            retry_a = raw_input("Enter Desired Option: ")
            if retry_a.lower() == 'a':
                self.reserve_seat()
            elif retry_a.lower() == 'b':
                gui_display()
            else:
                print "Wrong Input. Program will return to MAIN MENU in 5 seconds"
                x = 5
                while x != 0:
                    print str(x)
                    time.sleep(1)
                    x -= 1
                gui_display()
        elif self.menuHolder.lower() == 'b':
            print """
    A. MODIFY another seat
    B. Go to MAIN MENU
            """
            retry_b = raw_input("Enter Desired Option: ")
            if retry_b.lower() == 'a':
                self.modify_seat()
            elif retry_b.lower() == 'b':
                gui_display()
            else:
                print "Wrong Input. Program will return to MAIN MENU in 5 seconds"
                x = 5
                while x != 0:
                    print str(x)
                    time.sleep(1)
                    x -= 1
                gui_display()
        elif self.menuHolder.lower() == 'c':
            print """
    A. CANCEL another seat
    B. Go to MAIN MENU
            """
            retry_c = raw_input("Enter Desired Option: ")
            if retry_c.lower() == 'a':
                self.cancel_seat()
            elif retry_c.lower() == 'b':
                gui_display()
            else:
                print "Wrong Input. Program will return to MAIN MENU in 5 seconds"
                x = 5
                while x != 0:
                    print str(x)
                    time.sleep(1)
                    x -= 1
                gui_display()
        elif self.menuHolder.lower() == 'd':
            print """
    A. REFRESH
    B. Go to MAIN MENU
            """
            retry_d = raw_input("Enter Desired Option: ")
            if retry_d.lower() == 'a':
                self.display_seat_chart()
            elif retry_d.lower() == 'b':
                gui_display()
            else:
                print "Wrong Input. Program will return to MAIN MENU in 5 seconds"
                x = 5
                while x != 0:
                    print str(x)
                    time.sleep(1)
                    x -= 1
                gui_display()

airplane_one = AirplaneSeats()


def gui_display():
    os.system('cls')
    print """<<<Airplane Seat Reservation System>>>

    A. Reserve Seat
    B. Modify or Change Reserved Seat
    C. Cancel a Reserved Seat
    D. Display Seat Reservation Chart
    E. Exit
    """
    clientInput = raw_input("Enter Option: ")

    if clientInput.lower() == 'a':
        airplane_one.menuHolder = 'a'
        airplane_one.reserve_seat()
    elif clientInput.lower() == 'b':
        airplane_one.menuHolder = 'b'
        airplane_one.modify_seat()
    elif clientInput.lower() == 'c':
        airplane_one.menuHolder = 'c'
        airplane_one.cancel_seat()
    elif clientInput.lower() == 'd':
        airplane_one.menuHolder = 'd'
        airplane_one.display_seat_chart()
    elif clientInput.lower() == 'e':
        print "Program will exit"
        raw_input("<Press Enter>")
        exit()
    else:
        os.system('cls')
        print "You typed something not given"
        raw_input("<Press Enter>")
        gui_display()


def Main():
    gui_display()

if __name__ == '__main__':
    Main()
