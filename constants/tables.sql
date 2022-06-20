show databases;

use mysql;

CREATE TABLE DATASET_1
(
    CODE       TEXT      NOT NULL,
    VALUE      INT       NOT NULL,
    TIME_SAVED TIMESTAMP NOT null,
    constraint DATASET_1_CH check (DATASET_1.value >= 0)
);

CREATE TABLE DATASET_2
(
    CODE       TEXT      NOT NULL,
    VALUE      INT       NOT NULL,
    TIME_SAVED TIMESTAMP NOT null,
    constraint DATASET_2_CH check (DATASET_2.value >= 0)
);

CREATE TABLE DATASET_3
(
    CODE       TEXT      NOT NULL,
    VALUE      INT       NOT NULL,
    TIME_SAVED TIMESTAMP NOT null,
    constraint DATASET_3_CH check (DATASET_3.value >= 0)
);

CREATE TABLE DATASET_4
(
    CODE       TEXT      NOT NULL,
    VALUE      INT       NOT NULL,
    TIME_SAVED TIMESTAMP NOT null,
    constraint DATASET_4_CH check (DATASET_4.value >= 0)
);