all: dockerbuilddbint dockerpushdbint dockerbuildtemp dockerpushtemp manifest

dockerbuilddbint: #dbint/src/main.py
	docker build -t us.gcr.io/fred-hsu-veos/skodb:0.2 dbint
	
dockerpushdbint: #dbint/src/main.py
	docker push us.gcr.io/fred-hsu-veos/skodb:0.2

dockerbuildtemp: #temp/src/main.py
	docker build -t us.gcr.io/fred-hsu-veos/skotemp:0.2 temp
	
dockerpushtemp: #temp/src/main.py
	docker push us.gcr.io/fred-hsu-veos/skotemp:0.2

manifest:
	scp dbint-svc.yaml kube-138:
	scp dbint-az.yaml 13.66.200.155:

# makes yaml file available at https://s3-us-west-2.amazonaws.com/ceos-cni-demo/ceos-cni.yaml
manifestpush:
	aws s3 cp ceos-cni.yaml s3://ceos-cni-demo/ceos-cni.yaml --acl public-read-write
	aws s3 cp ceos-pod.yaml s3://ceos-cni-demo/ceos-pod.yaml --acl public-read-write
	aws s3 cp ceos-cni-ds.yaml s3://ceos-cni-demo/ceos-cni-ds.yaml --acl public-read-write
	aws s3 cp ceos-cni-split.yaml s3://ceos-cni-demo/ceos-cni-split.yaml --acl public-read-write
	aws s3 cp ceos-cni-cloud.yaml s3://ceos-cni-demo/ceos-cni-cloud.yaml --acl public-read-write
	aws s3 cp ceos-cni-eth.yaml s3://ceos-cni-demo/ceos-cni-eth.yaml --acl public-read-write
	aws s3 cp ceos-nocni-bgponly.yaml s3://ceos-cni-demo/ceos-nocni-bgponly.yaml --acl public-read-write
	$(info access at https://s3-us-west-2.amazonaws.com/ceos-cni-demo/ceos-cni.yaml)
	$(info access at https://s3-us-west-2.amazonaws.com/ceos-cni-demo/ceos-cni-ds.yaml)
	$(info access at https://s3-us-west-2.amazonaws.com/ceos-cni-demo/ceos-cni-cloud.yaml)
	$(info access at https://s3-us-west-2.amazonaws.com/ceos-cni-demo/ceos-cni-eth.yaml)

