import abc
import pyvisa


class Instrument(abc.ABC):
    """
    class defining a base instrument for using with pyvisa

    This class defines the base functionality expected for all VISA
    Instruments. To keep this manageable, it defines only the base commands
    all SCPI instruments will have implemented:

    *CLS - Clear Status
    *ESE - Event Status Enable
    *ESE? - Event Status Enable Query
    *ESR? - Event Status Enable Register
    *IDN? - Identify
    *OPC - Operation complete command
    *OPC? - Operation complete query
    *OPT? - Identify Options Query
    *RST - Reset
    *SRE - Service Request Enable
    *SRE? - Service Request Enable Query
    *STB? - Status Byte Query
    *TST? - Result of Self-test Query
    *WAI - Wait
    """

    def __init__(self, address, **kwargs):
        """
        Initialize a pyVISA object

        Parameters
        ----------
        address : str
            a visa resource string, or an ip address
        kwargs : dict
            visa_library (str), timemout in milliseconds (int), card_number
            (int), interface (str)

        Keyword Arguments
        -----------------
        resource_manager : (optional) pass in a shared pyvisa resource manager
            if required.
        visa_library : str
            allows pyvisa to use different visa_library backends, including the
            python-based pyvisa-py.  backend which can handle SOCKET and Serial
            (though not GPIB) connections.  It should be possible to use this
            library without NI-VISA libraries installed if the analyzer is so
            configured.
        timeout : int
            milliseconds
        interface : str
            one of "SOCKET", "GPIB"
        card_number : int
            for GPIB, default is usually 0
        """

        rm = kwargs.get("resource_manager", None)
        if not rm:
            rm = pyvisa.ResourceManager(visa_library=kwargs.get("visa_library", ""))

        interface = str(kwargs.get("interface", None)).upper()  # GPIB, SOCKET
        if interface == "GPIB":
            board = str(kwargs.get("card_number", "")).upper()
            resource_string = "GPIB{:}::{:}::INSTR".format(board, address)
        elif interface == "SOCKET":
            port = str(kwargs.get("port", 5025))
            resource_string = "TCPIP0::{:}::{:}::SOCKET".format(address, port)
        else:
            resource_string = address
        self.resource = rm.open_resource(resource_string)  # type: pyvisa.resources.messagebased.MessageBasedResource
        self.resource.timeout = kwargs.get("timeout", 3000)

        self.resource.read_termination = "\n"  # most queries are terminated with a newline
        self.resource.write_termination = "\n"
        if "instr" in resource_string.lower():
            self.resource.control_ren(2)

        # convenience pyvisa functions
        self.write = self.resource.write
        self.read = self.resource.read
        self.query = self.resource.query
        self.query_values = self.resource.query_values

    def __enter__(self):
        """
        context manager entry point
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        context manager exit point
        """
        self.resource.close()

    def close(self):
        self.__exit__(None, None, None)

    @property
    def idn(self):
        return self.query("*IDN?")

    def clear_status(self):
        self.write("*CLS")

    def set_event_status_enable(self):
        self.write("*ESE")
    
    def query_event_status_enable(self):
        self.query("*ESE?")

    def query_event_status_register(self):
        self.query("*ESR?")

    def set_wait_until_finished(self):
        self.query("*OPC")

    def wait_until_finished(self):
        self.query("*OPC?")

    def reset(self):
        self.write("*RST")
    
    def set_service_request_enable(self):
        self.write("*SRE")

    def query_service_request_enable(self):
        self.query("*SRE?")

    def query_status_byte(self):
        self.query("*STB?")
    
    def self_test_result(self):
        self.query("*TST?")
    
    def wait(self):
        self.write("*WAI")
