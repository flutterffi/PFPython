"""Standard library lesson 05: a small sqlite3 workflow."""

import sqlite3
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    database_path = project_root / "data" / "practice.db"

    connection = sqlite3.connect(database_path)
    try:
        cursor = connection.cursor()
        cursor.execute("drop table if exists sessions")
        cursor.execute(
            """
            create table sessions (
                id integer primary key,
                topic text not null,
                minutes integer not null
            )
            """
        )
        cursor.executemany(
            "insert into sessions(topic, minutes) values (?, ?)",
            [("functions", 25), ("decorators", 35), ("sqlite", 40)],
        )
        connection.commit()

        rows = cursor.execute(
            "select topic, minutes from sessions order by minutes desc"
        ).fetchall()
        for topic, minutes in rows:
            print(f"{topic}: {minutes} minutes")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
