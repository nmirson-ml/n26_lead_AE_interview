import unittest
from unittest.mock import patch
import subprocess

class TestKafkaConnectDeployment(unittest.TestCase):

    @patch('subprocess.run')
    def test_deploy_connector(self, mock_subprocess_run):
        mock_subprocess_run.return_value = subprocess.CompletedProcess(args=[], returncode=0)
        subprocess.run(["./kafka_connect/deploy_connector.sh"])
        mock_subprocess_run.assert_called_once()

if __name__ == '__main__':
    unittest.main()
