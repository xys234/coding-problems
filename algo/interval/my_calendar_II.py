"""
Implement a MyCalendarTwo class to store your events.
A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end).
Formally, this represents a booking on the half open interval [start, end),
the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection
(ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without
causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation:
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

# brute force works

"""

class MyCalendarTwo:

    def __init__(self):
        self.__overlaps = []
        self.__calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.__overlaps:
            if start < j and end > i:
                return False
        for i, j in self.__calendar:
            if start < j and end > i:
                self.__overlaps.append((max(start, i), min(end, j)))
        self.__calendar.append((start, end))
        return True




if __name__ == '__main__':

    obj = MyCalendarTwo()
    # case = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    # case = [[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]]
    # case = [[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
    # case = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
    # case = [[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25], [8,17], [24,33], [23,28], [21, 27]]
    # case = [[0,1],[20,21],[94,95],[0,1]]
    case = [[33,44],[85,95],[20,37],[91,100],[89,100],[77,87],[80,95],[42,61],[40,50],[85,99],[74,91],
             [70,82],[5,17],[77,89],[16,26],[21,31],[30,43],[96,100],[27,39],[44,55],[15,34],[85,99],
             [74,93],[84,94],[82,94],[46,65],[31,49],[58,73],[86,99],[73,84],[68,80],[5,18],[75,87],
             [88,100],[25,41],[66,79],[28,41],[60,70],[62,73],[16,33]]   # 60-70 should be false
    for e in case:
        print(obj.book(e[0], e[1]))