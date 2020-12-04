
class task_base_one_validation:
    def __init__(self):
        self.maximum_flights=0
        self.maximum_flight_time=0

    def validate_flight(self,time,flyed=None):
        if time <= self.maximum_flight_time:
            return time
        else :
            return self.maximum_flight_time

class A(task_base_one_validation):
    '''
        5.7.11.1. Task A (Last flight)
        Each competitor has an unlimited number of flights, but only the last flight is taken into account to
        determine the final result. The maximum flight time is limited to 300 seconds. Any subsequent
        launch of the model glider annuls the previous time.
        Working time: 7 minutes or 10 minutes 
    '''
    def __init__(self):
        super().__init__()
        self.maximum_flights=1
        self.maximum_flight_time=300


class A2(task_base_one_validation):

    def __init__(self):
        super().__init__()
        self.maximum_flights=1
        self.maximum_flight_time=300


class B(task_base_one_validation):
    '''
        5.7.11.2. Task B (Next to last and last flight)
        Each competitor has an unlimited number of flights, but only the next to last and the last flight will be
        scored.
        Maximum time per flight is 240 seconds for 10 minutes working time. If the number of competitors
        is large, the maximum flight time may be reduced to 180 seconds and 7 minutes working time.
        Example: 1st flight 65 s
        2nd flight 45 s
        3rd flight 55 s
        4th flight 85 s
        Total score: 55 s + 85 s = 140 s 
    '''
    def __init__(self):
        super().__init__()
        self.maximum_flights=2
        self.maximum_flight_time=240
       
class B2(task_base_one_validation):

    def __init__(self):
        super().__init__()
        self.maximum_flights=2
        self.maximum_flight_time=180

class C(task_base_one_validation):
    '''
            5.7.11.3. Task C (All up, last down)
            All competitors of a group must launch their model gliders simultaneously, within 3 seconds of the
            acoustic signal. The maximum measured flight time is 180 seconds.
            The official timekeeper takes the individual flight time of the competitor according to 5.7.6 and
            5.7.7 from the release of the model glider and not from the start of the acoustic signal. Launching
            a model glider before or more than 3 seconds after the start of the acoustic signal will result in a
            zero score for the flight.
            The number of launches (3 to 5) must be announced by the organiser before the contest begins.
            The preparation time between attempts is limited to 60 seconds after the end of the landing
            window. During this time the competitor may not perform test flights.
            The competitor is not allowed any help during the flight testing time, working time or landing
            window.
            The flight times of all attempts of each competitor will be added together and will be normalised to
            calculate the final score for this task.
            No working time is necessary.
            Example for 3 flights:
            Competitor A: 45 s + 50 s + 35 s = 130 s = 812.50 points
            Competitor B: 50 s + 50 s + 60 s = 160 s = 1000.00 points
            Competitor C: 30 s + 80 s + 40 s = 150 s = 937.50 points 
    '''
    def __init__(self):
        super().__init__()
        self.maximum_flights=3
        self.maximum_flight_time=180

class C2(task_base_one_validation):

    def __init__(self):
        super().__init__()
        self.maximum_flights=5
        self.maximum_flight_time=180


class D(task_base_one_validation):

    '''
        5.7.11.4. Task D (Two flights)
        Each competitor has two (2) flights. These two flights will be added together. The maximum
        accounted single flight time is 300 seconds. Working time is 10 minutes. 
    '''
    def __init__(self):
        super().__init__()
        self.maximum_flights=2
        self.maximum_flight_time=300

class E():

    '''
        5.7.11.5. Task E (Poker - variable target time)
        Each competitor has an unlimited number of flights to achieve or exceed up to three (3) target
        times. Before the first launch of a new target, each competitor announces a target time to the
        official timekeeper. He can then perform an unlimited number of launches to reach or exceed, this
        time.
        If the target is reached or exceeded, then the target time is credited and the competitor can
        announce the next target time, which may be lower, equal or higher, before he releases the model 
        Class F3K Hand Launch Gliders
        SC4_Vol_F3_Soaring_20 Effective 1st January 2020 Page 37
        glider during the launch.
        If the target time is not reached, the announced target flight time cannot be changed. The
        competitor may try to reach the announced target flight time until the end of the working time. For
        the competitors last flight he may announce “end of working time”. For this specific call, the
        competitor has ONLY one attempt.
        The target time must be announced clearly in the official contest language or alternatively shown
        to the timekeeper in written numbers (e g 2:38) by the competitor’s helper immediately after the
        launch. If the competitor calls “end of working time” the competitor’s helper writes the letter “W”.
        The target(s) (1 - 3) with achieved target times are scored. The achieved target times are added
        together.
        This task may be included in the competition program only if the organiser provides a sufficient
        number of official timekeepers, so that each competitor in the round is accompanied by one official
        timekeeper.
        The working time may be 10 or 15 minutes.
        Example: Announced time Flight time Scored time
        45 s 1st flight 46 s 45 s
        50 s 1st flight 48 s 0 s
        2nd flight 52 s 50 s
        47 s 1st flight 49 s 47 s
        Total score is 142 s 
    '''
    def __init__(self):
        self.maximum_flights=3
        self.maximum_flight_time=599


    def validate_flight(self,time=None,flyed=None):
        flyed=float(flyed)
        if flyed:
            if time+flyed<=self.maximum_flight_time:
                return time
            else:
                if self.maximum_flight_time-flyed == 0:
                    return 0
                else:
                    return self.maximum_flight_time-flyed
        else:
            if time <= self.maximum_flight_time:
                return time
            else :
                return self.maximum_flight_time




class E2(E):

    def __init__(self):
        super().__init__()
        self.maximum_flights=3
        self.maximum_flight_time=899

class F(task_base_one_validation):

    def __init__(self):
        super().__init__()
        self.maximum_flights=3
        self.maximum_flight_time=180
    '''
        5.7.11.6. Task F (3 out of 6)
        During the working time, the competitor may launch his model glider a maximum of 6 times. The
        maximum accounted single flight time is 180 s. The sum of the three longest flights up to the
        maximum of 180 s for each flight is taken for the final score.
        Working time is 10 minutes.
    '''

class G(task_base_one_validation):

    def __init__(self):
        super().__init__()
        self.maximum_flights=5
        self.maximum_flight_time=120
    '''
        5.7.11.7. Task G (Five longest flights)
        Each competitor has an unlimited number of flights. Only the best five flights will be added
        together. The maximum accounted single flight time is 120 seconds.
        Working time is 10 minutes.
    '''

class H(task_base_one_validation):
# TO DO CORRECT VALIDATION !!! 
    def __init__(self):
        super().__init__()
        self.maximum_flights=4
        self.maximum_flight_time=999
    '''
        5.7.11.8. Task H (One, two, three and four minute target flight times, any order)
        During the working time, each competitor has an unlimited number of flights. He has to achieve
        four flights each of different target flight times duration.
        The target flight times are 60, 120, 180 and 240 seconds in any order. Thus the competitor’s four
        longest flights flown in the working time are assigned to the four target flight times, so that his
        longest flight is assigned to the 240 seconds target flight time, his 2nd longest flight to the 180
        seconds target flight time, his 3rd longest flight to the 120 seconds target flight time and his 4th
        longest flight to the 60 seconds target flight time.
        Only the flight time up to the target flight time is taken into account for scoring.
        Working time is 10 minutes.
        Example: Flight time Scored time
        1st flight 63 s 60 s
        2nd flight 239 s 239 s
        3rd flight 182 s 180 s
        4th flight 90 s 90 s
        Total score of this task would be 60 s + 239 s + 180 s + 90 s = 569 s
    '''

class I(task_base_one_validation):
# TO DO CORRECT VALIDATION !!! 
    def __init__(self):
        super().__init__()
        self.maximum_flights=3
        self.maximum_flight_time=200
    '''
        5.7.11.9 Task I (Three longest flights)
        During the working time, each competitor has an unlimited number of flights. 
        Class F3K Hand Launch Gliders
        SC4_Vol_F3_Soaring_20 Effective 1st January 2020 Page 38
        Only the best three flights will be added together. The maximum accounted single flight is 200
        seconds.
        Working time is 10 minutes.
    '''

class J(task_base_one_validation):

    def __init__(self):
        super().__init__()
        self.maximum_flights=3
        self.maximum_flight_time=180
    '''
        5.7.11.10 Task J (Three last flights)
        During the working time, each competitor has an unlimited number of flights, but only the three last
        flights will be scored.
        Maximum time per flight is 180 seconds for 10 minutes working time.
        Example: 1st flight 150 s
        2nd flight 45 s
        3rd flight 180 s
        4th flight 150 s
        Total score: 45 s + 180 s + 150 s = 375 s
    '''

class K(task_base_one_validation):
# TO DO CORRECT VALIDATION !!! 
    def __init__(self):
        super().__init__()
        self.maximum_flights=5
        self.maximum_flight_time=999
    '''
        5.7.11.11 Task K (Increasing time by 30 seconds, “Big Ladder”)
        Each competitor must launch his/her model glider exactly five (5) times to achieve five (5) target
        times as follows: 1:00 (60 seconds), 1:30 (90 seconds), 2:00 (120 seconds), 2:30 (150 seconds),
        3:00 (180 seconds). The targets must be flown in the increasing order as specified. The actual
        times of each flight up to (not exceeding) the target time will be added up and used as the final
        score for the task. The competitors do not have to reach or exceed the target times to count each
        flight time.
        Working time: 10 minutes.
    '''

class L(task_base_one_validation):

    def __init__(self):
        super().__init__()
        self.maximum_flights=1
        self.maximum_flight_time=599
    '''
        5.7.11.12 Task L (One flight)
        During the working time, the competitor may launch his model glider one single time. The
        maximum flight time is limited to 599 seconds (9 minutes 59 seconds).
        Working time: 10 minutes.
    '''

class M(task_base_one_validation):
# TO DO CORRECT VALIDATION !!! 
    def __init__(self):
        super().__init__()
        self.maximum_flights=3
        self.maximum_flight_time=999
    '''
        5.7.11.13 Fly-off Task M (Increasing time by 2 minutes “Huge Ladder”)
        Each competitor must launch his/her model glider exactly three (3) times to achieve three (3) target
        times as follows: 3:00 (180 seconds), 5:00 (300 seconds), 7:00 (420 seconds). The targets must
        be flown in the increasing order as specified. The actual times of each flight up to (not exceeding)
        the target time will be added up and used as the final score for the task. The competitors do not
        have to reach or exceed the target times to count each flight time.
        Working time: 15 minutes. 
    '''