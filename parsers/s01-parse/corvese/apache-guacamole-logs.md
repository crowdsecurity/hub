# Description
A parser that will search for failed authentication attempts. 

# Configuration
- Modify the `acquis.yaml` configuraiton file. The `type` **MUST** be exactly as shown here or the parser will never be successful.

```yaml
filenames:
  - /path/to/apache-guacamole.log
labels:
  type: apache-guacamole
```
:exclamation: The `type` **MUST** be `apache-guacamole` :exclamation:

# Apache Quacamole configuration

The default log format used by quacamole is not supported by crowdsec as there is no date in the log line you will need to do the following to make it compatible, these are examples and should be changed to reflect your setup.

- Create the following 'logback.xml' file in guacamole home dir to log with the correct Date format.
STDOUT
```
<configuration>
    <!-- Default appender -->
    <appender name="GUAC-DEFAULT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%date{"yyyy-MM-dd'T'HH:mm:ss,SSSXXX", UTC} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- Log at INFO level -->
    <root level="WARN">
        <appender-ref ref="GUAC-DEFAULT" />
    </root>

</configuration>
```

FILE:
```
<configuration>
    <!-- Default appender -->
    <appender name="GUAC-DEFAULT" class="ch.qos.logback.core.FileAppender">
        <file>/var/log/guacamole.log</file>
        <encoder>
            <pattern>%date{"yyyy-MM-dd'T'HH:mm:ss,SSSXXX", UTC} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- Log at INFO level -->
    <root level="WARN">
        <appender-ref ref="GUAC-DEFAULT" />
    </root>

</configuration>
```

If using docker you will need to mount the following volume that links to the logback.xml file and set the GUACAMOLE_HOME variable
```
    volumes:
    - ./logback.xml:/home/guacamole/temp/logback.xml:ro
    environment:
      GUACAMOLE_HOME: /home/guacamole/temp/
```
