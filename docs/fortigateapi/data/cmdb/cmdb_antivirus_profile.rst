cmdb/antivirus/profile
----------------------

FortiOS v6.4.14

.. code:: yaml

    analytics-bl-filetype: 0
    analytics-db: disable
    analytics-max-upload: 10
    analytics-wl-filetype: 0
    av-block-log: enable
    av-virus-log: enable
    cifs:
      archive-block: ''
      archive-log: ''
      emulator: enable
      options: ''
      outbreak-prevention: disabled
    comment: Scan files and block viruses.
    content-disarm:
      cover-page: enable
      detect-only: disable
      error-action: log-only
      office-action: enable
      office-dde: enable
      office-embed: enable
      office-hylink: enable
      office-linked: enable
      office-macro: enable
      original-file-destination: discard
      pdf-act-form: enable
      pdf-act-gotor: enable
      pdf-act-java: enable
      pdf-act-launch: enable
      pdf-act-movie: enable
      pdf-act-sound: enable
      pdf-embedfile: enable
      pdf-hyperlink: enable
      pdf-javacode: enable
    extended-log: disable
    feature-set: flow
    ftgd-analytics: disable
    ftp:
      archive-block: ''
      archive-log: ''
      emulator: enable
      options: scan
      outbreak-prevention: disabled
    http:
      archive-block: ''
      archive-log: ''
      content-disarm: disable
      emulator: enable
      options: scan
      outbreak-prevention: disabled
    imap:
      archive-block: ''
      archive-log: ''
      content-disarm: disable
      emulator: enable
      executables: virus
      options: scan
      outbreak-prevention: disabled
    mapi:
      archive-block: ''
      archive-log: ''
      emulator: enable
      executables: default
      options: ''
      outbreak-prevention: disabled
    mobile-malware-db: enable
    nac-quar:
      expiry: 5m
      infected: none
      log: disable
    name: default
    nntp:
      archive-block: ''
      archive-log: ''
      emulator: enable
      options: ''
      outbreak-prevention: disabled
    outbreak-prevention:
      external-blocklist: disable
      ftgd-service: disable
    pop3:
      archive-block: ''
      archive-log: ''
      content-disarm: disable
      emulator: enable
      executables: virus
      options: scan
      outbreak-prevention: disabled
    q_origin_key: default
    replacemsg-group: ''
    scan-mode: default
    smtp:
      archive-block: ''
      archive-log: ''
      content-disarm: disable
      emulator: enable
      executables: virus
      options: scan
      outbreak-prevention: disabled
    ssh:
      archive-block: ''
      archive-log: ''
      emulator: enable
      options: ''
      outbreak-prevention: disabled
