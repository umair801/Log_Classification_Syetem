import re

def classify_with_regex(log_message):
    regex_patterns = {
        # User Actions
        r"User User\d+ logged (in|out).": "User Action",
        r"Account with ID .* created by .*": "User Action",  # .*: zero or more of any character
        
        # System Notifications
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        
        # # HTTP Status
        # r"nova\..*\.wsgi\.server \[req-[\w-]+\]": "HTTP Status",

        # Critical Errors
        r"System component is not operating: .*": "Critical Error",
        r"Detection of multiple failed disks in RAID setup": "Critical Error",
        r"Irreparable failure detected in .*": "Critical Error",

        # Security Alerts
        r"Admin privilege elevation warning for user \d+": "Security Alert",
        r"Invalid credentials used for account .*": "Security Alert",
        r"Server \d+ is under potential security threat, .*": "Security Alert",

        # Errors
        r"Module .* experienced an invalid data format issue": "Error",
        r"Data replication for shard \d+ encountered an issue": "Error",
        r"Shard \d+ replication task ended in failure": "Error",

        # # Resource Usage
        # r"nova\.compute\.(claims|resource_tracker) \[req-[\w -]+]": "Resource Usage",

        # Workflow Errors
        r"Customer follow-up process for lead ID \d+ failed.*": "Workflow Error",
        r"Task assignment for TeamID \d+ could not complete.*": "Workflow Error",
        r"Lead conversion failed for prospect ID \d+ due to .*": "Workflow Error",

        # Deprecation Warnings
        r"API endpoint .* is deprecated.*": "Deprecation Warning",
        r"The '.*' feature is outdated.*": "Deprecation Warning",
        r"Support for .* authentication methods will be removed.*": "Deprecation Warning",
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None

    
if __name__ == "__main__":
    test_sentences = [
        # Resource Usage
        "nova.compute.claims [req-6a763803-4838-49c7-81...] Allocating resources.",
        "nova.compute.resource_tracker [req-addc1839-2e...] Checking disk usage.",
        
        # HTTP Status
        "nova.metadata.wsgi.server [req-61196723-e034-4...] GET request received.",
        "nova.osapi_compute.wsgi.server [req-d4353962-c...] Processing request.",
        
        # # System Notification
        # "Backup completed successfully.",
        # "Backup Completed Successfully.",
        # "Backup started at 12:30 AM.",
        # "Backup ended at 02:00 AM.",
        # "System updated to version 3.2.1.",
        # "File report.pdf uploaded successfully by user JohnDoe.",
        # "Disk cleanup completed successfully.",
        # "System reboot initiated by user Admin2.",

        # # User Action
        # "Account with ID 1234 created by User1.",
        # "Account with ID 5678 created by Admin1.",
        # "User User123 logged in.",
        # "User User45 logged out.",
        
        # # Critical Error
        # "System component is not operating: component ID 23.",
        # "Detection of multiple failed disks in RAID setup.",
        # "Irreparable failure detected in fundamental application service.",
        
        # # Security Alert
        # "Admin privilege elevation warning for user 8634.",
        # "Invalid credentials used for account Account473.",
        # "Server 40 is under potential security threat, immediate action required.",
        
        # # Error
        # "Module X experienced an invalid data format issue.",
        # "Data replication for shard 6 encountered an issue.",
        # "Shard 4 replication task ended in failure.",
        
        # # Workflow Error
        # "Customer follow-up process for lead ID 5621 failed due to timeout.",
        # "Task assignment for TeamID 3425 could not complete successfully.",
        # "Lead conversion failed for prospect ID 7842 due to missing data.",
        
        # # Deprecation Warning
        # "API endpoint 'getCustomerDetails' is deprecated. Use 'getClientData' instead.",
        # "The 'ExportToCSV' feature is outdated. Please switch to 'ExportToExcel'.",
        # "Support for legacy authentication methods will be removed in the next update.",
        
        # # Random/Unclassified
        # "Hey Bro, chill ya!",
        # "User John sent a message.",
        # "The server is down, please check.",
        # "Rebooting the system now...",
        # "User logged a bug in the system.",
        # "Hello there! How are you?"
    ]

    for sentence in test_sentences:
        print(classify_with_regex(sentence))
