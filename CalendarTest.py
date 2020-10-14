import sys
import unittest
import datetime
from unittest.mock import Mock, patch
# Add other imports here if needed
import calendar

from Calendar import Calendar





class CalendarTest(unittest.TestCase):

    # This test tests number of upcoming events.
    def test_get_upcoming_events_number(self):
        num_events = 2
        time = "2020-08-03T00:00:00.000000Z"

        mock_api = Mock()
        calendar = Calendar()
        events = calendar.get_upcoming_events(mock_api, time, num_events)
        # events = calendar.get_upcoming_events(mock_api, time, num_events)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1
        )

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['maxResults'], num_events)

    # @patch('Calendar.open')
    # def test_two_year_event_future(self, mock_api):
    #     cal = Calendar()
    #
    #     # args, kwargs = mock_api.events.return_value.list.call_args_list[0]
    #     # starting_time = time_now = datetime.datetime.utcnow().isoformat() + 'Z'
    #     # ending_time = (datetime.datetime.utcnow() + datetime.timedelta(days=2 * 365)).isoformat() + 'Z'
    #
    #     mock_api.events.list.execute.return_value=[]
    #     event = cal.get_two_year_event_future(mock_api)
    #     print(event)
    #
    #     # self.assertEqual(
    #     #     mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1
    #     # )
    #     # self.assertEqual(kwargs['timeMin'][0:19], starting_time[0:19])
    #     # self.assertEqual(kwargs['timeMax'][0:19], ending_time[0:19])




    @patch('Calendar.open')
    def test_five_year_event_past(self, mock_api):
        cal = Calendar()
        event = cal.get_five_year_event_past(mock_api)

        expected_value= [{'event_summary': 'arshia', 'reminders': {'useDefault': True}}]

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        ending_time = datetime.datetime.utcnow().isoformat() + 'Z'
        starting_time = (datetime.datetime.utcnow() - datetime.timedelta(days=5 * 365)).isoformat() + 'Z'
        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1
        )
        mock_api.events.list.execute.return_value = [{'event_summary': 'arshia', 'reminders': {'useDefault': True}}]
        self.assertEqual(kwargs['timeMin'][0:20], starting_time[0:20])
        self.assertEqual(kwargs['timeMax'][0:20], ending_time[0:20])
        print(kwargs)
        self.assertEqual(mock_api.events.list.execute(), expected_value
        )

    @patch('Calendar.open')
    def test_two_year_event_future(self, mock_api):
        cal = Calendar()
        event = cal.get_two_year_event_future(mock_api)

        expected_value= [{'event_summary': 'arshia', 'reminders': {'useDefault': True}}]

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        starting_time = datetime.datetime.utcnow().isoformat() + 'Z'
        ending_time = (datetime.datetime.utcnow() + datetime.timedelta(days=2 * 365)).isoformat() + 'Z'
        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1
        )
        mock_api.events.list.execute.return_value = [{'event_summary': 'arshia', 'reminders': {'useDefault': True}}]
        self.assertEqual(kwargs['timeMin'][0:20], starting_time[0:20])
        self.assertEqual(kwargs['timeMax'][0:20], ending_time[0:20])
        print(kwargs)
        self.assertEqual(mock_api.events.list.execute(), expected_value
        )


    @patch('Calendar.open')
    def test1(self, mock_api):
        cal = Calendar()
        event = cal.get_five_year_event_past(mock_api)
        expected_value = [1, 2, 3]
        mock_api.events.list.execute.return_value = [1, 2, 3]
        print(mock_api.events.list.execute())

    @patch('Calendar.open')
    def test_delete_event_valid(self, mock_api):
        with patch('Calendar.open') as mock_event:
            cal = Calendar()
            # mock_event = Mock()
            event = cal.get_five_year_event_past(mock_api)
            mock_event.events.delete.return_value = [{'event_summary': 'arshia', 'reminders': {'useDefault': True}}]
            self.assertEqual(cal.delete_event(mock_api, mock_event, 0), "Success")

    @patch('Calendar.open')
    def test_delete_event_outOfIndex(self, mock_api):#delete_event(api, event, index)
        with patch('Calendar.open') as mock_event:
            cal = Calendar()
            # mock_event = Mock()
            event = cal.get_five_year_event_past(mock_api)
            mock_event.events.delete.return_value = [{'event_summary': 'arshia', 'reminders': {'useDefault': True}}]
            self.assertEqual(cal.delete_event(mock_api, mock_event, 1000000000000), "out of index")


    @patch('Calendar.open')
    def test_delete_event_negativeIndex(self, mock_api):#delete_event(api, event, index)
        with patch('Calendar.open') as mock_event:
            cal = Calendar()
            # mock_event = Mock()
            event = cal.get_five_year_event_past(mock_api)
            mock_event.events.delete.return_value = [{'event_summary': 'arshia', 'reminders': {'useDefault': True}}]
            self.assertEqual(cal.delete_event(mock_api, mock_event, -10), "Negative index")





    # # # Add more test cases here
    # @patch('Calendar.open')
    # def test1(self, mock_api):
    #     num_events = 2
    #     time = "2020-08-03T00:00:00.000000Z"
    #
    #     calendar = Calendar()
    #     events = calendar.get_five_year_event_past(mock_api)
    #     events = calendar.get_two_year_event_future(mock_api)
    #     self.assertEqual(
    #         mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 2
    #     )
    #     print(mock_api.events.return_value.list.call_args_list[0])
    #     print(mock_api.events.return_value.list.call_args_list[1])
    #     # print(mock_api.events.return_value.list.call_args_list[2])
    #     print(mock_api.events.return_value.list.return_value.execute.return_value)
    #     calendar.delete_reminder(mock_api, events, 0, 1000)

    # @patch('Calendar.open')
    # def two_year_event_future(self, mock_api):
    #
    #     cal = Calendar()
    #     event = cal.get_two_year_event_future(mock_api)
    #
    #     args, kwargs = mock_api.events.return_value.list.call_args_list[0]
    #     starting_time = time_now = datetime.datetime.utcnow().isoformat() + 'Z'
    #     ending_time = (datetime.datetime.utcnow() + datetime.timedelta(days=2 * 365)).isoformat() + 'Z'
    #     self.assertEqual(kwargs['timeMin'], starting_time)
    #     self.assertEqual(kwargs['timeMax'], ending_time)


def main():

    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(CalendarTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)


main()
