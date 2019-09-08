# LocationLock

Inspired by the TV show Agents of Shield, I decided to recreate a bit of technology they used in the show, location based encryption.
The user should run the mobile client, which is downloadable from the Google Play Store: https://play.google.com/store/apps/details?id=com.craigmsirota.lockdown. The user should also run the lockdown.py script. This program allows the user to send location data from their cell phone to their computer, which would be running the app. After receiving a password on both ends, the program encrypts/decrypts the requested file.

The file can either be used by running the the python script with the files to encrypt/decrypt as command line arguments or it will prompt the user with a file browser window.

The encryption currently only works on plaintext files, including .txt files, .py files, .c files, etc.
