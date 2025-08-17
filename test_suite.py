import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from analytics_dashboard import (
    get_user_growth_data,
    get_revenue_data,
    get_engagement_data,
    get_kpi_data,
    get_activity_feed,
    export_report
)

class TestAnalyticsDashboard(unittest.TestCase):
    def setUp(self):
        self.start_date = datetime.now() - timedelta(days=30)
        self.end_date = datetime.now()

    @patch('analytics_dashboard.get_user_data')
    def test_get_user_growth_data(self, mock_get_user_data):
        mock_get_user_data.return_value = [
            {'date': self.start_date, 'total_users': 100},
            {'date': self.start_date + timedelta(days=7), 'total_users': 120},
            {'date': self.start_date + timedelta(days=14), 'total_users': 150},
            {'date': self.start_date + timedelta(days=21), 'total_users': 180},
            {'date': self.end_date, 'total_users': 200}
        ]
        data = get_user_growth_data(self.start_date, self.end_date)
        self.assertEqual(len(data), 5)
        self.assertEqual(data[0]['total_users'], 100)
        self.assertEqual(data[-1]['total_users'], 200)

    @patch('analytics_dashboard.get_revenue_data')
    def test_get_revenue_data(self, mock_get_revenue_data):
        mock_get_revenue_data.return_value = [
            {'date': self.start_date, 'revenue': 10000},
            {'date': self.start_date + timedelta(days=7), 'revenue': 12000},
            {'date': self.start_date + timedelta(days=14), 'revenue': 14000},
            {'date': self.start_date + timedelta(days=21), 'revenue': 16000},
            {'date': self.end_date, 'revenue': 18000}
        ]
        data = get_revenue_data(self.start_date, self.end_date)
        self.assertEqual(len(data), 5)
        self.assertEqual(data[0]['revenue'], 10000)
        self.assertEqual(data[-1]['revenue'], 18000)

    @patch('analytics_dashboard.get_engagement_data')
    def test_get_engagement_data(self, mock_get_engagement_data):
        mock_get_engagement_data.return_value = [
            {'date': self.start_date, 'active_sessions': 1000},
            {'date': self.start_date + timedelta(days=7), 'active_sessions': 1200},
            {'date': self.start_date + timedelta(days=14), 'active_sessions': 1400},
            {'date': self.start_date + timedelta(days=21), 'active_sessions': 1600},
            {'date': self.end_date, 'active_sessions': 1800}
        ]
        data = get_engagement_data(self.start_date, self.end_date)
        self.assertEqual(len(data), 5)
        self.assertEqual(data[0]['active_sessions'], 1000)
        self.assertEqual(data[-1]['active_sessions'], 1800)

    @patch('analytics_dashboard.get_user_data')
    @patch('analytics_dashboard.get_revenue_data')
    @patch('analytics_dashboard.get_engagement_data')
    def test_get_kpi_data(self, mock_get_user_data, mock_get_revenue_data, mock_get_engagement_data):
        mock_get_user_data.return_value = [
            {'date': self.start_date, 'total_users': 100},
            {'date': self