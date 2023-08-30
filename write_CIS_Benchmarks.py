from hardening_CIS_Benchmarks import PolicyCopier

# ruta del ejecutable LGPO.exe
ruta_lgpo = r"LGPO\LGPO.exe"

# ruta destino a donde se va a realizar la copias de la políticas de archivos .admx
ruta_destino_x = r"C:\\Windows\\PolicyDefinitions"

# ruta destino a donde se va a realizar la copias de la políticas de archivos .adml
ruta_destino_l = r"C:\\Windows\\PolicyDefinitions\\en-US"


class Hardening:

    @staticmethod
    def hardening_adobe():
        """
        Adobe
        """
        # ruta de los archivos .admx
        ruta1_adobe_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Adobe\AcrobatDCContinuous.admx"
        ruta2_adobe_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Adobe\AcrobatProDCContinuous.admx"
        # ruta de los archivos .adml
        ruta1_adobe_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Adobe\en-us\AcrobatDCContinuous.adml"
        ruta2_adobe_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Adobe\en-us\AcrobatProDCContinuous.adml"
        # ruta de los archivos ejecutables
        ruta1_adobe_e = r"STIG_GPO_Package_July_2023\DoD Adobe Acrobat Reader DC Continuous V2R1\GPOs\{45606343-8AFB-48D5-848E-2A6D22B3BA70}"
        ruta2_adobe_e = r"STIG_GPO_Package_July_2023\DoD Adobe Acrobat Reader DC Continuous V2R1\GPOs\{BFDDF882-A145-4758-B1B5-F8A207880C61}"

        # llamando la clase hardening_CIS_Benchmarks
        PolicyCopier(ruta1_adobe_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta2_adobe_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta1_adobe_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta2_adobe_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier.write_policies(ruta_lgpo, ruta1_adobe_e)
        PolicyCopier.write_policies(ruta_lgpo, ruta2_adobe_e)

    @staticmethod
    def hardening_chrome():
        """
        Chrome
        """
        # ruta de los archivos .admx
        ruta1_chrome_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Google\chrome.admx"
        ruta2_chrome_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Google\google.admx"
        ruta3_chrome_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Google\GoogleUpdate.admx"
        # ruta de los archivos .adml
        ruta1_chrome_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Google\en-US\chrome.adml"
        ruta2_chrome_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Google\en-US\google.adml"
        ruta3_chrome_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Google\en-US\GoogleUpdate.adml"
        # ruta de los archivos ejecutables
        ruta1_chrome_e = r"STIG_GPO_Package_July_2023\DoD Google Chrome v2r8\GPOs\{0FBEE738-6902-4E7E-8E79-9A0B1B2668B9}"

        # se llama la clase hardening_CIS_Benchmarks para copiar los políticas
        PolicyCopier(ruta1_chrome_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta2_chrome_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta3_chrome_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta1_chrome_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta2_chrome_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta3_chrome_l, ruta_destino_l).copy_policies_adm()
        # se realiza la escritura de la políticas
        PolicyCopier.write_policies(ruta_lgpo, ruta1_chrome_e)

    @staticmethod
    def hardening_edge():
        """
        Edge
        """
        # ruta de los archivos .admx
        ruta1_edge_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Microsoft Edge\msedge.admx"
        ruta2_edge_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Microsoft Edge\msedgeupdate.admx"
        ruta3_edge_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Microsoft Edge\msedgewebview2.admx"
        # ruta de los archivos .adml
        ruta1_edge_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Microsoft Edge\en-US\msedge.adml"
        ruta2_edge_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Microsoft Edge\en-US\msedgeupdate.adml"
        ruta3_edge_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Microsoft Edge\en-US\msedgewebview2.adml"
        # ruta de los archivos ejecutables
        ruta1_edge_e = r"STIG_GPO_Package_July_2023\DoD Microsoft Edge v1r7\GPOs\{7121E30A-6426-45FA-9DA0-3C60AA4C130A}"

        # se llama la clase hardening_CIS_Benchmarks para copiar los políticas
        PolicyCopier(ruta1_edge_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta2_edge_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta3_edge_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta1_edge_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta2_edge_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta3_edge_l, ruta_destino_l).copy_policies_adm()
        # se realiza la escritura de la políticas
        PolicyCopier.write_policies(ruta_lgpo, ruta1_edge_e)

    @staticmethod
    def hardening_office365():
        """
        Office 365
        """
        # ruta de los archivos .admx
        ruta1_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\access16.admx"
        ruta2_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\excel16.admx"
        ruta3_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\lync16.admx"
        ruta4_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\office16.admx"
        ruta5_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\onent16.admx"
        ruta6_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\outlk16.admx"
        ruta7_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\ppt16.admx"
        ruta8_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\proj16.admx"
        ruta9_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\pub16.admx"
        ruta10_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\teams16.admx"
        ruta11_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\visio16.admx"
        ruta12_office_x = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\word16.admx"
        # ruta de los archivos .adml
        ruta1_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\access16.adml"
        ruta2_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\excel16.adml"
        ruta3_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\lync16.adml"
        ruta4_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\office16.adml"
        ruta5_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\onent16.adml"
        ruta6_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\outlk16.adml"
        ruta7_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\ppt16.adml"
        ruta8_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\proj16.adml"
        ruta9_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\pub16.adml"
        ruta10_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\teams16.adml"
        ruta11_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\visio16.adml"
        ruta12_office_l = r"STIG_GPO_Package_July_2023\ADMX Templates\Office 2016-2019-M365\en-us\word16.adml"
        # ruta de los archivos ejecutables
        ruta1_office_e = r"STIG_GPO_Package_July_2023\DoD Office 2019-M365 Apps v2r8\GPOs\{53C5F5C7-724B-45FF-B0B1-4CCDCE7B1560}"
        ruta2_office_e = r"STIG_GPO_Package_July_2023\DoD Office 2019-M365 Apps v2r8\GPOs\{C4F9D4E8-CB46-4527-991F-1D8671AE1E32}"

        # se llama la clase hardening_CIS_Benchmarks para copiar los políticas
        PolicyCopier(ruta1_office_x,ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta2_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta3_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta4_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta5_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta6_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta7_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta8_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta9_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta10_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta11_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta12_office_x, ruta_destino_x).copy_policies_adm()
        PolicyCopier(ruta1_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta2_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta3_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta4_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta5_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta6_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta7_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta8_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta9_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta10_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta11_office_l, ruta_destino_l).copy_policies_adm()
        PolicyCopier(ruta12_office_l, ruta_destino_l).copy_policies_adm()
        # se realiza la escritura de la políticas
        PolicyCopier.write_policies(ruta_lgpo, ruta1_office_e)
        PolicyCopier.write_policies(ruta_lgpo, ruta2_office_e)

    @staticmethod
    def hardening_windows_10():
        """
        windows 10
        """
        # ruta de los archivos ejecutables
        ruta1_win10_e = "STIG_GPO_Package_July_2023\DoD Windows 10 v2r6\GPOs\{710F47EE-3F73-4C89-B9F4-9C3F6E3DA7C5}"
        ruta2_win10_e = "STIG_GPO_Package_July_2023\DoD Windows 10 v2r6\GPOs\{A4BAA70C-1584-4D5C-B433-C97C0B5E52FC}"
        # se realiza la escritura de la políticas
        PolicyCopier.write_policies(ruta_lgpo, ruta1_win10_e)
        PolicyCopier.write_policies(ruta_lgpo, ruta2_win10_e)

    @staticmethod
    def hardening_windows_11():
        """
        windows 11
        """
        # ruta de los archivos ejecutables
        ruta1_win11_e = "STIG_GPO_Package_July_2023\DoD Windows 11 v1r3\GPOs\{B6EE9320-BB96-47B1-9254-B6F845DAC6A8}"
        ruta2_win11_e = "STIG_GPO_Package_July_2023\DoD Windows 11 v1r3\GPOs\{E6064767-DDA0-4532-826B-D13FBA0BC9F2}"
        # se realiza la escritura de la políticas
        PolicyCopier.write_policies(ruta_lgpo, ruta1_win11_e)
        PolicyCopier.write_policies(ruta_lgpo, ruta2_win11_e)
