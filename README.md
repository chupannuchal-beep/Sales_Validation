# Sales_Validation

========================================================================
                      SYSTEM WORKFLOW EXPLANATION
========================================================================

1. Connection Established
   - Establishes connection to either the local or remote FTP server (FileZilla on XAMPP) through host credentials, username, and password.
   - Modifies status indicator to show connectivity status.

2. Folders Selection
   - Configures the user-specified working pathways:
     * Download directory where temporary incoming files are stored.
     * Archive directory to where clean and valid files are moved.
     * Errors directory where invalid files and errors occur.

3. File Server (Server Browser)
   - Retrieves and shows all available files stored in the remote FTP directory.
   - Offers real-time search and filter capabilities to find target files.

4. File Selection
   - Identifies the CSV file stored in the remote server directory that is to be validated.

5. Validation
   - Conducts a series of health tests on the selected file:
     * Filename format validation (timestamp Regex validation).
     * File size validation (identifying files with zero bytes).
     * CSV schema header validation.
     * Completeness and uniqueness validation (duplicate IDs).
     * Dates and financial row-level calculation validation.

6. Process File
   - Downloads file and redirects to either archive or errors folder based 
     on the validation results:
     * Clean files are moved to the Archive folder automatically.
     * Invalid files are moved to the Errors folder automatically.

7. Error Logs
   - Creates formatted error logs in the `validation_errors.log` 
     when the file fails validation checks.
   - Contains exact timestamps, filenames, error types, error descriptions, and 
     unique UUID token.

8. Activity Clean
   - Shows activity messages within the Activity Feed window.
   - Provides a single click button named "Clear Activity Feed" that clears 
     the screen history completely.
