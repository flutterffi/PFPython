"""Project 03: store study sessions in sqlite and print a summary."""

import sqlite3
from pathlib import Path


def database_path() -> Path:
    return Path(__file__).resolve().parents[1] / "data" / "study_tracker.db"


def main() -> None:
    connection = sqlite3.connect(database_path())
    try:
        cursor = connection.cursor()
        cursor.execute("drop table if exists study_sessions")
        cursor.execute(
            """
            create table study_sessions (
                id integer primary key,
                topic text not null,
                minutes integer not null
            )
            """
        )
        cursor.executemany(
            "insert into study_sessions(topic, minutes) values (?, ?)",
            [("loops", 20), ("typing", 30), ("sqlite", 45)],
        )
        connection.commit()

        total_minutes = cursor.execute(
            "select coalesce(sum(minutes), 0) from study_sessions"
        ).fetchone()[0]
        longest = cursor.execute(
            "select topic, minutes from study_sessions order by minutes desc limit 1"
        ).fetchone()

        print(f"total_minutes = {total_minutes}")
        print(f"longest_session = {longest}")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
