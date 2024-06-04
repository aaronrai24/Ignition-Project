from java.awt import Color
from java.awt import Font
from javax.swing import BorderFactory
from com.inductiveautomation.ignition.common.gui.border import PanelTitledBorder
from com.inductiveautomation.ignition.common.gui.border import ButtonBorder

def window(title='', border_color='shared.ui.color.primary_lighter', background_color='shared.ui.color.background'):
	border_color = eval(border_color)
	background_color = eval(background_color)
	
	border = PanelTitledBorder(border_color, background_color, title)
	border.setStyle(PanelTitledBorder.STYLE_PLAIN)
	border.setHGap(8)
	border.setShadowSize(2)
	
	if len(title) == 0:
		border.setVGap(0)
	else:
		border.setVGap(3)
		
	return border