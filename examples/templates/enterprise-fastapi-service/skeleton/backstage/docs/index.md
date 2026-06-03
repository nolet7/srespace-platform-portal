
${{ values.name }}
Overview

${{ values.description }}

Ownership
Field	Value
Owner	${{ values.owner }}
Lifecycle	${{ values.lifecycle }}
System	${{ values.system }}
Repository	${{ values.repoOwner }}/${{ values.repoName }}
Endpoints
Endpoint	Purpose
/	Service information
/health	Liveness check
/ready	Readiness check
/metrics	Prometheus metrics
