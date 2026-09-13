--
-- PostgreSQL database dump
--

\restrict tqF2q6GZ6XpJU1DE7iw8GkP4alQkocmE8o7zcfvwgOCcvcJ8eRDRIGsdaIONzm1

-- Dumped from database version 16.15
-- Dumped by pg_dump version 16.15

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE IF EXISTS ONLY public.records DROP CONSTRAINT IF EXISTS records_pkey;
DROP TABLE IF EXISTS public.records;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: records; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.records (
    id bigint NOT NULL,
    title character varying(200) NOT NULL,
    CONSTRAINT records_title_check CHECK ((length(TRIM(BOTH FROM title)) > 0))
);


--
-- Name: records_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.records ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.records_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: records; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.records (id, title) FROM stdin;
1	Review service readiness
2	Document the operating procedure
3	testing write
4	Persistence proof
5	Validation proof 1789231597
6	Validation proof 1789231726
7	Validation proof
8	Validation persistence proof
\.


--
-- Name: records_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.records_id_seq', 8, true);


--
-- Name: records records_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.records
    ADD CONSTRAINT records_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict tqF2q6GZ6XpJU1DE7iw8GkP4alQkocmE8o7zcfvwgOCcvcJ8eRDRIGsdaIONzm1

