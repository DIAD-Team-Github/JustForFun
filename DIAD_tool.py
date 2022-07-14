import arcpy
import sys
sys.path.insert(0,"D:\Work\AGO_Tools\DIAD_Toolbox")


class DIADTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "DIAD Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        

        in_file = arcpy.Parameter(
            displayName="Input field",
            name="in_field",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")
        
        params = [in_file]

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
		
	
    def execute(self, parameters, messages):
        """The source code of the tool."""

        arcpy.AddMessage("New tool run")

        return
