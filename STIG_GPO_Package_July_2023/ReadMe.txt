WARNING
-------

It must be noted that the Group Policy Objects (GPO) provided should be evaluated in a local, representative test environment before implementation within production environments. The extensive variety of environments makes it impossible to test these GPOs for all potential enterprise Active Directory and software configurations. For most environments, failure to test before implementation may lead to a loss of required functionality.

It is especially important to fully test with all GPOs against all Windows Operating Systems, internet browsers, specific and legacy applications which are targeted by each STIG GPO which are currently used in the environment.


INTRODUCTION
------------

This package contains ADMX template files, GPO backups exports, GPO reports, and WMI filter exports. It is to provide enterprise administrators the supporting GPOs and related files to aid them in the deployment of GPOs within their enterprise to meet STIG settings. Administrators are expected to fully test GPOs in test environments prior to live production deployments.


MAINTENANCE
-----------

This package will be updated with each quarterly release of STIG updates. If a targeted STIG within the package is released out of cycle, the package will be updated accordingly. Additionally, if a new STIG is targeted to provide a supporting GPO, the package will be updated to include GPO backup, GPO report, and checklist file and ADMX and WMI filter exports as required.

With declaration of sundown of Windows 8.1 STIGs in April 2018, the Windows 8.1 GPOs and supporting files will no longer be updated. The April 2018 GPOs and supporting files will remain part of the baseline package and will not be updated.

With declaration of Windows 7 and Windows Server 2008 R2 end of life as of January 14, 2020, the Windows 7 and Windows Server 2008 R2 supporting files have been removed from GPO package.

April 2020, added Microsoft Office 2019 and Microsoft Office 365 Pro Plus.

June 2020
Removed OneDrive for Business and OneDrive NextGen from ADMX Templates. These are duplicate files and contained deprecated settings. A single OneDrive directory was added that contains the single current ADMX/L template files. 

Added update Office2016/2019/O365 ADMX/L files.

Windows Server 2016 DC & MS User GPO has been added to meet new STIG requirements.

Windows Server 2019 DC & MS User GPO has been added to meet new STIG requirements.

Out-of-cycle Windows 8 and 8.1 STIG update required update to Windows 8 and 8.1 GPOs.

October 2020
Added Support files - contains files to assist administrator to automate the import of DISA GPOs in test of production environments.

DISA_STIG_GPO_Import.docx - contain instructions for execution of DISA_GPO_BASELINE_IMPORT.PS1 script.

DISA_GPO_BASELINE_IMPORT.PS1 - PowerShell script to import DISA STIG GPOs.

DISA_AllGPO_Import_Oct2020.csv - Import file to be used if all DISA STIG GPOs are to be imported to test or production environments. PowerShell script will prompt user to overwrite each GPO if already present in environment. Intended to be used in new environment or overwrite all existing DISA STIG GPOs.

DISA_QuarterlyGPO_MMMYYY_Import.csv - Import file to be used to only import quarterly DISA STIG GPO updates for the quarter or out-of-cycle release. Intended to be used for quarterly or out-of-cycle release to import only those GPOs modified for the package release.

importtable.migtable - A blank migration table required when importing operating system STIG GPOs. Administrator must enter the appropriate values (DOMAINNAME\Domain Admins & DOMAINNAME\Enterprise Admins) to replace the entries "ADD YOUR DOMAIN ADMINS" and "ADD YOUR ENTERPRISE ADMINS". Administrators should restrict any equivalent delegate groups within their domain GPOs.

Local Policies - Contain GPO backups of Windows operating systems to be used to apply STIG configurations via local policy. Intended to be used for standalone systems. 

Sample_LGPO.bat - A sample batch file to apply local policies GPOs to stand alone systems.

February 2021
Added Microsoft Edge GPO and ADMX/ADML template files to package. - Proxy server settings require administrators to configure appropriate local site proxy server configurations.

April 2021
Added MSIntunePolicies_Beta to package - contains Intune JSON backup files to assist administrators in evaluating baseline configurations to support Microsoft Intune.

July 2021
Added Adobe Acrobat Reader DC Continuous to package.

January 2022
Added Mozilla Firefox GPO policies to package.

July 2022
Added Windows 11 GPO to package.
Removed Microsoft Endpoint Manager policies from GPO package. A separate MEM policy STIG package will contain MEM policies.

Oct 2022
Added Windows Server 2022 GPO to package.
Restored Intune Baseline policies to GPO package.

July 2023
Prior to July 2023 release, the policy value Computer Configuration > Administrative Templates > System > Remote Procedure Call > Restricted Unauthenticated RPC client was configured within the DoD WinSvr 2016 DC STIG Comp vXrX and DoD WinSvr 2022 DC STIG Comp vXrX GPOs. The setting has been removed from the DoD WinSvr 2016 DC STIG Comp vXrX and DoD WinSvr 2022 DC STIG Comp vXrX GPOs to match DoD WinSvr 2012 R2 DC STIG Comp vXrX and DoD WinSvr 2019 DC STIG Comp vXrX.
Applying any local policy member server Computer STIG GPO to a system will configure this setting. Promoting system prior to removing this setting will allow setting to remain configured. It is the systems administrator's responsibility to review and remove any delta configurations between local policy member server configurations and the domain controller policies.


USAGE
-----

This package is to be used to assist administrators implementing STIG settings within their environment. The administrator must fully test GPOs in test environments prior to live production deployments. The GPOs provided contain most applicable and restrictive GPO STIG settings contained in STIG files. 

The GPO backups are located under the GPO directory in the parent STIG directory. Administrators will be required to modify operating system GPOs to reflect the appropriate Enterprise Admins and Domain Admins groups for User Rights Assignments. The GPOs contain ADD YOUR ENTERPRISE ADMINS and ADD YOUR DOMAIN ADMINS text. These can be modified during import of GPO backups if a migration table is used or after import is complete. 

GPOs are split into computer configuration and user configuration where possible. Each GPO has only the appropriate section enabled within the configured GPO. For example, in a GPO identified as a Computer GPO, the User Configuration section of GPO is disabled. 

The Office System 2013 and Office System 2016 GPOs contain the IE Security settings from each of the components because of GPO application and precedence.

The WMI Filter files are located under the WMI Filter directory in the parent STIG directory. The provided WMI filter exports files are sample WMI filters that can be used to apply to the matching GPO to target the desired operating system or application. A single WMI filter, Microsoft Office C2R.mof, is intended for Microsoft Office 2019 and Microsoft Office 365 ProPlus.

The provided GPO reports provide the administrator ability to review GPO configuration from a browser.

Delta spreadsheet reports provide the differences between current and previous STIG GPOs.

KNOWN ISSUES
------------
The Windows Server 2012 R2, Windows Server 2016, and Windows Server 2019 member server GPO are configured to the strictest setting (Local Account instead of Local account and member of Administrators group) for user right assignments values. The setting Deny access to this computer from the network must be relaxed to Local account and member of Administrators group on a system attempting to configure as member of cluster.

Windows 11 STIG ID V-253303 is set to a value of 14. The STIG requirement of 15 characters is not supported via GPO configuration. To achieve this configuration, sites must deploy a Fine Grain Password Policy within the environment.