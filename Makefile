.PHONY: build

build:
	sam build
    
deploy-site:
	aws-vault exec my-user --no-session -- aws s3 sync ../cloud-resume-frontend s3://craigs-cloud-resume-challenge
    
deploy-infra:
	sam build && aws-vault exec my-user --no-session -- sam deploy
