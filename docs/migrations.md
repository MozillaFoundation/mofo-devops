# Database Migration Checklist

When upgrading or downgrading a database, use this checklist to reduce the chance of data loss.

1. Download latest backup and restore it to a local postrges database
2. Verify data integrity of the backup
3. Proceed depending on service (Heroku, AWS RDS)
    1. **Heroku PostgreSQL**
        1. [Here is a script that can automate the process detailed below](https://gist.github.com/cadecairos/4ca05411f1156c2b6303b010d0f74f14)
        2. Enable maintenance mode on the app
        3. Scale the app's dynos to 0
        4. Initiate the automated migration using `heroku pg:copy`
        5. Remove the old database plan
        6. Set the new Database URL config value to `DATABASE_URL` (or the key name the app expects)
        7. Scale the dynos back up
        8. Disable maintenance mode
    1. **AWS RDS**
        1. Create a read replica of the desired size and wait for it to catch up
        2. Promote the read replica to be the master database
        3. Update the database connection string of the application
