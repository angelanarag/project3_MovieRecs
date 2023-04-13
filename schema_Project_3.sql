-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/M70Zx2
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "db_revenue" (
    "id" INT   NOT NULL,
    "title" CHAR(255)   NOT NULL,
    "genre" CHAR(255)   NOT NULL,
    "language" CHAR(2)   NOT NULL,
    "release_date" Date   NOT NULL,
    "budget" BIGINT   NOT NULL,
    "revenue" BIGINT   NOT NULL,
    "rating" FLOAT   NOT NULL,
    "vote_count" INT   NOT NULL,
    CONSTRAINT "pk_db_revenue" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "db_crew" (
    "id" INT   NOT NULL,
    "name" CHAR(255)   NOT NULL,
    "gender" INT   NOT NULL,
    "popularity" FLOAT   NOT NULL,
    CONSTRAINT "pk_db_crew" PRIMARY KEY (
        "id"
     )
);

