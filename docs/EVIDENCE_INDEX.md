# Evidence and submission index

- Repository URL: https://github.com/AnassEhab33/Barq-academy-devops-intern.git
- Final commit: 700e0a4f001b2968214c75d1d6a1747025477ca5
- Matching CI run: https://github.com/AnassEhab33/Barq-academy-devops-intern/actions/runs/34879677904
- Continuous 12-18 minute video URL: https://drive.google.com/file/d/1xE6P3F5ZbfDgPIt2__7syR2vpmP1OSkY/view?usp=sharing
- Challenge receipt ID: 972ee5656016433284732e18268fcaf1
- Starting video commit: d384a8ebf454834af8388edc8c44c6d99fe0b323
- Later documentation-only commits, if any: I pushed (9c79c60aefff1af31d0d698a39d6bbc8c481fa7e) in the video but, it didn't work because, the problem i discussed in the video and said i will fix it after the video and fixed it in those commits (5e50599362f43409369e0aa916cb175f5b4225e2 , 700e0a4f001b2968214c75d1d6a1747025477ca5)

For each requirement, link: file/output -> commit -> video timestamp.
Match the final README, diagram, GitHub code and video (three instances, public port 8090).


## Requirements → Evidence
| Video Timestamp | Task | Commit | Affected Files |
| --- | --- | --- | --- |
| 0:00 - 0:58 | Introducing My self | _ | _ |
| 0:58 - 1:36 | Show your repository, starting commit and clean git status | `c8d8f15` | _ |
| 1:36 - 2:46 | Build/start the stopped environment; show service health. Prebuilt images are allowed. | _ | `docker-compose.yml`, `Dockerfile` |
| 2:46 - 3:52 | Test /, /health, /ready, /records and /counter. | _ | `validate.py` |
| 3:52 - 4:34 | Use /instance to prove both backends serve repeated requests through NGINX. | _ | `nginx/nginx.conf` |
| 4:34 - 6:12 | Stop one backend. Show continued traffic and errors; recover it and prove it serves again. | _ | `failure_test.py` |
| 6:12 - 8:16 | Show a created record surviving app and PostgreSQL container recreation. | _ | `docker-compose.yml`, `database/init.sql` |
| 8:16 - 9:10 | Run validation and the failure test. Demonstrate one historical-log finding. | _ | `validate.py`, `failure_test.py`, `log_analysis.md` |
| 9:10 - 11:41 | Run ./video_challenge.sh once, for the first time in this video working copy. | _ | `video_challenge.sh`, `troubleshooting.md` |
| 11:41 - 15:26 | Change public port 8080 to 8090 live. Prove NGINX works on 8090. | _ | `.env`, `docker-compose.yml` |
| 15:26 - 19:00 | Add a third app instance live. Prove all three respond; rerun validation. | _ | `docker-compose.yml`, `nginx/nginx.conf`, `validate.py` |
| 19:00 - 20:00 | Run git status and git diff. Explain changes, commit on screen and show commit hashes. | _ | _ |
| 20:00 - 21:00 | Push video commits. Link each change to its commit and video timestamp. | `9c79c60` | _ |