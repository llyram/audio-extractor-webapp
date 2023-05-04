# Manifests

The `manifests` directory contains the following YAML files:

```
manifests
├── auth-deploy.yaml
├── configmap.yaml
├── secret.yaml
└── service.yaml
```

Each of these files defines a specific Kubernetes resource for the `auth` service. 

- `auth-deploy.yaml`: deployment configuration for the `auth` service
- `configmap.yaml`: configuration data for the `auth` service
- `secret.yaml`: secret data (e.g. passwords) for the `auth` service
- `service.yaml`: service configuration for the `auth` service

You can apply these manifests to your Kubernetes cluster using the `kubectl apply` command. For example, to apply the `auth-deploy.yaml` file, you can run:

```
kubectl apply -f manifests/auth-deploy.yaml
``` 

Make sure to apply the files in the correct order, as some files (such as `auth-deploy.yaml`) may depend on resources defined in other files.