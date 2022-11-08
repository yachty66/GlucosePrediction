register_gitlab_runner:
	docker run --rm -it -v gitlab-runner-config:/etc/gitlab-runner gitlab/gitlab-runner:latest register


start_gitlab_runner:
	# create the config for the container
	docker volume create gitlab-runner-config
	# start the docker container
	docker run -d --name gitlab-runner --restart always \
     -v /var/run/docker.sock:/var/run/docker.sock \
     -v gitlab-runner-config:/etc/gitlab-runner gitlab/gitlab-runner:latest


stop_gitlab_container:
	# stop the old containers
	docker stop gitlab-runner && docker rm gitlab-runner
