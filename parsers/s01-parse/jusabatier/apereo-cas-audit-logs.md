Use Apereo CAS audit logs : https://apereo.github.io/cas/6.4.x/audits/Audits-File.html

Need to : 
* ativate `cas.audit.slf4j.use-single-line=true` in CAS configuration
* add cas_audit.log generated file to CrowdSec aquisitions

Sample log4j config : 

```xml
[...]
        <RollingFile name="auditlogfile" fileName="${baseDir}/cas_audit.log" append="true"
                     filePattern="${baseDir}/cas_audit-%d{yyyy-MM-dd-HH}-%i.log">
            <PatternLayout pattern="%d %p [%c] - %m%n"/>
            <Policies>
                <OnStartupTriggeringPolicy />
                <SizeBasedTriggeringPolicy size="10 MB"/>
                <TimeBasedTriggeringPolicy />
            </Policies>
        </RollingFile>

        <CasAppender name="casAudit">
            <AppenderRef ref="auditlogfile" />
        </CasAppender>
[...]
        <AsyncLogger name="org.apereo.inspektr.audit.support" level="info" includeLocation="true" >
            <AppenderRef ref="casAudit"/>
        </AsyncLogger>
[...]
```
