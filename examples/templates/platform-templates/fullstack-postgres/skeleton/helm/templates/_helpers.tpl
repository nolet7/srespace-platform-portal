{{/*
Return chart name.
*/}}
{{- define "app.name" -}}
{{- default .Chart.Name .Values.global.appName | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Return full application name.
*/}}
{{- define "app.fullname" -}}
{{- .Values.global.appName | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Return chart label.
*/}}
{{- define "app.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common labels.
*/}}
{{- define "app.labels" -}}
helm.sh/chart: {{ include "app.chart" . }}
app.kubernetes.io/name: {{ include "app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: {{ .Values.global.appName }}
backstage.io/owner: {{ .Values.global.owner | quote }}
{{- end -}}

{{/*
Selector labels.
*/}}
{{- define "app.selectorLabels" -}}
app.kubernetes.io/name: {{ include "app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/part-of: {{ .Values.global.appName }}
{{- end -}}
