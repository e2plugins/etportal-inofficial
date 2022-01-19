###########################################
#                                         #
#   Plugin: EtPortal (Inofficial)         #
#   Original EtPortal created by bla666   #
#                                         #
###########################################

from Plugins.Plugin import PluginDescriptor
from Components.PluginComponent import plugins
from Components.Label import Label
from Components.Pixmap import Pixmap
from enigma import ePicLoad, eTimer, getDesktop
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.InfoBarGenerics import InfoBarPlugins
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from Components.AVSwitch import AVSwitch
from Tools.Directories import fileExists, isPluginInstalled
from Components.ConfigList import ConfigListScreen
from Components.config import config, ConfigSubsection, ConfigBoolean, getConfigListEntry, ConfigYesNo, ConfigSelection, NoSave, ConfigNothing
from Screens.PluginBrowser import PluginBrowser
from Components.PluginList import *
from Components.Pixmap import MovingPixmap
from . import _

EtPortalVersion = '3.7'
SHARED_DIR_PATH = '/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/pics/'

IMAGE_SIZE = 128
IMAGE_SIZE_S = 128
IMAGE_SIZE_XS = 128
IMAGE_SIZE_XXS = 128
IMAGE_SPACE = 30
BORDER_OFFSET_SIZE = 100
NUMBER_OF_PICTURES = 7

baseInfoBarPlugins__init__ = None
global_index = 0
skin_w = getDesktop(0).size().width()

config.plugins.EtPortal = ConfigSubsection()
config.plugins.EtPortal.finalexit = ConfigBoolean(default=False)
config.plugins.EtPortal.rememberposition = ConfigYesNo(default=True)
config.plugins.EtPortal.showtimericon = ConfigBoolean(default=True)
config.plugins.EtPortal.enablemarkbutton = ConfigYesNo(default=True)
config.plugins.EtPortal.vfd = ConfigYesNo(default=True)
#config.plugins.EtPortal.adult = ConfigPassword(default='', visible_width=50, fixed_size=False)
config.plugins.EtPortal.Get = ConfigYesNo(default=False)
config.plugins.EtPortal.movie = ConfigYesNo(default=True)
config.plugins.EtPortal.emc = ConfigYesNo(default=False)
config.plugins.EtPortal.dvd = ConfigYesNo(default=False)
config.plugins.EtPortal.media = ConfigYesNo(default=False)
config.plugins.EtPortal.picture = ConfigYesNo(default=True)
config.plugins.EtPortal.iptv = ConfigYesNo(default=True)
config.plugins.EtPortal.weblinks = ConfigYesNo(default=True)
config.plugins.EtPortal.merlinmusic = ConfigYesNo(default=False)
config.plugins.EtPortal.foreca = ConfigYesNo(default=False)
config.plugins.EtPortal.tvspielfilm = ConfigYesNo(default=False)
config.plugins.EtPortal.extensions = ConfigYesNo(default=True)
config.plugins.EtPortal.pluginbrowser = ConfigYesNo(default=True)
config.plugins.EtPortal.shutdown = ConfigYesNo(default=True)
config.plugins.EtPortal.systeminfo = ConfigYesNo(default=True)
config.plugins.EtPortal.dreamexplorer = ConfigYesNo(default=True)
config.plugins.EtPortal.dreamplex = ConfigYesNo(default=False)
config.plugins.EtPortal.digitalfernsehen = ConfigYesNo(default=True)
config.plugins.EtPortal.Chefkoch = ConfigYesNo(default=True)
config.plugins.EtPortal.bluray = ConfigYesNo(default=True)
config.plugins.EtPortal.blurayconfig = ConfigSelection(default='List', choices=[('List', _('List')), ('Cover', _('Cover')), ('Cover_Full', _('Cover_Full'))])
config.plugins.EtPortal.bild = ConfigYesNo(default=True)
config.plugins.EtPortal.kinode = ConfigYesNo(default=True)
config.plugins.EtPortal.spiegel = ConfigYesNo(default=True)
config.plugins.EtPortal.focus = ConfigYesNo(default=True)
config.plugins.EtPortal.wiki = ConfigYesNo(default=True)
config.plugins.EtPortal.kicker = ConfigYesNo(default=False)
config.plugins.EtPortal.kickerticker = ConfigYesNo(default=False)
config.plugins.EtPortal.verkehrsinfo = ConfigYesNo(default=True)
config.plugins.EtPortal.turkvod = ConfigYesNo(default=False)
config.plugins.EtPortal.greekstreamtv = ConfigYesNo(default=False)
config.plugins.EtPortal.mediaportal = ConfigYesNo(default=True)
config.plugins.EtPortal.xtrend = ConfigYesNo(default=True)
config.plugins.EtPortal.networkbrowser = ConfigYesNo(default=True)
config.plugins.EtPortal.yamp = ConfigYesNo(default=True)
config.plugins.EtPortal.shoutcast = ConfigYesNo(default=True)
config.plugins.EtPortal.tunein = ConfigYesNo(default=True)
config.plugins.EtPortal.muzutv = ConfigYesNo(default=True)
config.plugins.EtPortal.facebook = ConfigYesNo(default=True)
config.plugins.EtPortal.ardhbbtv = ConfigYesNo(default=True)
config.plugins.EtPortal.skyrecorder = ConfigYesNo(default=True)
config.plugins.EtPortal.atvreader = ConfigYesNo(default=True)
config.plugins.EtPortal.tstube = ConfigYesNo(default=True)
config.plugins.EtPortal.kodi = ConfigYesNo(default=True)
config.plugins.EtPortal.mp3browser = ConfigYesNo(default=True)
config.plugins.EtPortal.moviebrowser = ConfigYesNo(default=True)
config.plugins.EtPortal.pvmc = ConfigYesNo(default=True)
config.plugins.EtPortal.webradiofs = ConfigYesNo(default=True)
config.plugins.EtPortal.powertimer = ConfigYesNo(default=True)
config.plugins.EtPortal.tvcharts = ConfigYesNo(default=False)
config.plugins.EtPortal.mediainfo = ConfigYesNo(default=True)
config.plugins.EtPortal.downloadcenter = ConfigYesNo(default=True)
config.plugins.EtPortal.fragmutti = ConfigYesNo(default=True)
config.plugins.EtPortal.moviearchiver = ConfigYesNo(default=True)
config.plugins.EtPortal.tanken = ConfigYesNo(default=True)
config.plugins.EtPortal.wikitv = ConfigYesNo(default=True)
config.plugins.EtPortal.hbbig = ConfigYesNo(default=True)
config.plugins.EtPortal.operabrowser = ConfigYesNo(default=True)
config.plugins.EtPortal.yahooweather = ConfigYesNo(default=True)
config.plugins.EtPortal.watchmi = ConfigYesNo(default=True)

config.plugins.EtPortal.none = NoSave(ConfigNothing()) 
config.plugins.EtPortal.color = ConfigSelection(default='SkinColor_HD', choices=[('ice_HD', _('ice_HD')), ('black_HD', _('black_HD')), ('Nobile_HD', _('Nobile_HD')), ('SkinColor_HD', _('SkinColor_HD')), ('Xion_HD', _('Xion_HD')), ('Xion_FullHD', _('Xion_FullHD')), ('Metrix_FullHD', _('Metrix_FullHD'))])


def writeToVFD(txt):
    if config.plugins.EtPortal.vfd.value:
        model = '/proc/stb/info/boxtype'
        oled = '/dev/dbox/oled0'
        if fileExists(oled):                   
            if fileExists(model):
                segmentled = open(model).read().strip() 
                if segmentled == 'odinm7': 
                    config.plugins.EtPortal.vfd.setValue(False)
                else:
                    tmp = open(oled, 'w')
                    tmp.write(txt[:124])
                    tmp.close()
            else:
                config.plugins.EtPortal.vfd.setValue(False)
        else:
            config.plugins.EtPortal.vfd.setValue(False)
            

class EtPortalScreen(Screen):
    def __init__(self, session):
        global global_index
        self.session = session
        self.textcolor = '#FFFFFF'
        self.color = '#30000000'
        skincontent = ''
        piclist = []
		
        if config.plugins.EtPortal.systeminfo.value:
            piclist.append(('information.png', _('System information')))
        if isPluginInstalled('DreamExplorer') and config.plugins.EtPortal.dreamexplorer.value:
            piclist.append(('dreamexplorer.png', _('DreamExplorer')))
        if isPluginInstalled('DreamPlex') and config.plugins.EtPortal.dreamplex.value:
            piclist.append(('dreamplex.png', _('DreamPlex')))
        if config.plugins.EtPortal.dvd.value and isPluginInstalled('DVDPlayer'):
            piclist.append(('dvd_player.png', _('DVD Player')))
        if config.plugins.EtPortal.media.value:
            piclist.append(('media_player.png', _('Media Player')))
        if isPluginInstalled('EnhancedMovieCenter') and config.plugins.EtPortal.emc.value:
            piclist.append(('emc.png', _('Enhanced Movie-Center')))
        if isPluginInstalled('PicturePlayer' ,'ui') and config.plugins.EtPortal.picture.value:
            piclist.append(('picture_player.png', _('Picture Player')))
        if isPluginInstalled('NetworkBrowser', 'NetworkBrowser') and config.plugins.EtPortal.networkbrowser.value:
            piclist.append(('network.png', _('Network Browser')))
        if isPluginInstalled('IPTV-List-Updater') and config.plugins.EtPortal.iptv.value:
            piclist.append(('iptv.png', _('IPTV-List Updater')))
        if isPluginInstalled('TVSpielfilm') and config.plugins.EtPortal.tvspielfilm.value:
            piclist.append(('tvspielfilm.png', _('TV Spielfilm')))
        if isPluginInstalled('OpenOpera') and config.plugins.EtPortal.operabrowser.value or isPluginInstalled('NXHbbTV') and config.plugins.EtPortal.operabrowser.value:
            piclist.append(('opera.png', _('Opera Browser')))
        if isPluginInstalled('OpenOpera') and config.plugins.EtPortal.wikitv.value or isPluginInstalled('NXHbbTV') and config.plugins.EtPortal.wikitv.value:
            piclist.append(('wikitv.png', _('Wiki Tv')))
        if isPluginInstalled('OpenOpera') and config.plugins.EtPortal.hbbig.value or isPluginInstalled('NXHbbTV') and config.plugins.EtPortal.hbbig.value:
            piclist.append(('hbbig.png', _('HBBig')))
        if isPluginInstalled('OpenOpera') and config.plugins.EtPortal.watchmi.value or isPluginInstalled('NXHbbTV') and config.plugins.EtPortal.watchmi.value:
            piclist.append(('watchmi.png', _('Themenkan\xc3\xa4le')))
        if isPluginInstalled('Weblinks') and config.plugins.EtPortal.weblinks.value:
            piclist.append(('weblinks.png', _('Weblinks plugin')))
        if isPluginInstalled('MerlinMusicPlayer') and config.plugins.EtPortal.merlinmusic.value:
            piclist.append(('merlinmusic.png', _('Merlin Music Player')))
        if isPluginInstalled('DIGITALfernsehen') and config.plugins.EtPortal.digitalfernsehen.value:
            piclist.append(('digitalfernsehen.png', _('DiGITAL fernsehen')))
        if isPluginInstalled('Foreca') and config.plugins.EtPortal.foreca.value:
            piclist.append(('foreca.png', _('Foreca Weather')))
        if isPluginInstalled('Chefkoch') and config.plugins.EtPortal.Chefkoch.value:
            piclist.append(('chefkoch.png', _('Chefkoch')))
        if isPluginInstalled('Blu-ray') and config.plugins.EtPortal.bluray.value:
            piclist.append(('bluray.png', _('BLURAY-DISC')))
        if isPluginInstalled('BILDOnline') and config.plugins.EtPortal.bild.value:
            piclist.append(('bild.png', _('Bild.de')))
        if isPluginInstalled('KINOde') and config.plugins.EtPortal.kinode.value:
            piclist.append(('kino.png', _('Kino.de')))
        if isPluginInstalled('SPIEGELOnline') and config.plugins.EtPortal.spiegel.value:
            piclist.append(('spiegel.png', _('Spiegel ONLINE')))
        if isPluginInstalled('FOCUSOnline') and config.plugins.EtPortal.focus.value:
            piclist.append(('focus.png', _('Focus ONLINE')))
        if isPluginInstalled('Wikipedia') and config.plugins.EtPortal.wiki.value:
            piclist.append(('wiki.png', _('Wikipedia')))
        if isPluginInstalled('MUZUtv') and config.plugins.EtPortal.muzutv.value:
            piclist.append(('muzutv.png', _('MUZU.TV')))
        if isPluginInstalled('clever-tanken') and config.plugins.EtPortal.tanken.value:
            piclist.append(('tanken.png', _('clever-tanken.de')))
        if isPluginInstalled('kicker') and config.plugins.EtPortal.kicker.value:
            piclist.append(('kicker.png', _('Kicker Online')))
        if isPluginInstalled('kicker') and config.plugins.EtPortal.kickerticker.value:
            piclist.append(('kickerticker.png', _('Kicker Live-Ticker')))
        if isPluginInstalled('verkehrsinfo') and config.plugins.EtPortal.verkehrsinfo.value:
            piclist.append(('verkehrsinfo.png', _('Verkehrsinfo.de')))
        if isPluginInstalled('Facebook') and config.plugins.EtPortal.facebook.value:
            piclist.append(('facebook.png', _('Facebook')))
        if isPluginInstalled('TURKvod') and config.plugins.EtPortal.turkvod.value:
            piclist.append(('turkvod.png', _('TURKvod IPTV')))
        if isPluginInstalled('GreekStreamTV') and config.plugins.EtPortal.greekstreamtv.value:
            piclist.append(('greekstreamtv.png', _('Greek StreamTV')))
        if isPluginInstalled('MediaPortal') and config.plugins.EtPortal.mediaportal.value:
            piclist.append(('mediaportal.png', _('MediaPortal')))
        if isPluginInstalled('OpenXtaReader') and config.plugins.EtPortal.xtrend.value:
            piclist.append(('xtrend.png', _('OpenXTA Forum Reader')))
        if isPluginInstalled('YampMusicPlayer') and config.plugins.EtPortal.yamp.value:
            piclist.append(('yamp.png', _('Yamp Music Player')))
        if isPluginInstalled('SHOUTcast') and config.plugins.EtPortal.shoutcast.value:
            piclist.append(('shoutcast.png', _('SHOUTcast')))
        if isPluginInstalled('OpenOpera') and config.plugins.EtPortal.tunein.value or isPluginInstalled('NXHbbTV') and config.plugins.EtPortal.tunein.value:
            piclist.append(('tunein.png', _('tunein Radio')))
        if isPluginInstalled('OpenOpera') and config.plugins.EtPortal.ardhbbtv.value or isPluginInstalled('NXHbbTV') and config.plugins.EtPortal.ardhbbtv.value:
            piclist.append(('ardhbbtv.png', _('ARD HbbTV-Portal')))
        if isPluginInstalled('skyrecorder') and config.plugins.EtPortal.skyrecorder.value:
            piclist.append(('skyrecorder.png', _('sky recorder')))
        if isPluginInstalled('MP3Browser') and config.plugins.EtPortal.mp3browser.value:
            piclist.append(('mp3browser.png', _('mp3-Browser')))
        if isPluginInstalled('MovieBrowser') and config.plugins.EtPortal.moviebrowser.value:
            piclist.append(('moviebrowser.png', _('Movie-Browser')))
        if isPluginInstalled('ProjectValerie') and config.plugins.EtPortal.pvmc.value:
            piclist.append(('valerie.png', _('Project-Valerie')))
        if isPluginInstalled('webradioFS') and config.plugins.EtPortal.webradiofs.value:
            piclist.append(('webradiofs.png', _('WebRadioFS')))
        if config.plugins.EtPortal.showtimericon.value:
            piclist.append(('timer.png', _('Timers for recordings')))
        if config.plugins.EtPortal.movie.value:
            piclist.append(('movie_player.png', _('Movie Player')))
        if config.plugins.EtPortal.extensions.value:
            piclist.append(('extensions_plugins.png', _('Extension Plugins and applications')))
        if config.plugins.EtPortal.pluginbrowser.value:
            piclist.append(('plugins.png', _('Plugin Browser')))
        if config.plugins.EtPortal.shutdown.value:
            piclist.append(('shutdown.png', _('Sleeptimer and power control')))
        #if fileExists('/usr/lib/enigma2/python/Screens/PowerTimerEdit.pyo') and 
        if config.plugins.EtPortal.powertimer.value:
            piclist.append(('powertimer.png', _('Power Timer')))
        if isPluginInstalled('TVCharts') and config.plugins.EtPortal.tvcharts.value:
            piclist.append(('tvcharts.png', _('TV Charts')))
        if isPluginInstalled('MediaInfo') and config.plugins.EtPortal.mediainfo.value:
            piclist.append(('mediainfo.png', _('MediaInfo')))
        if isPluginInstalled('downloadcenter') and config.plugins.EtPortal.downloadcenter.value:
            piclist.append(('downloadcenter.png', _('DownloadCenter')))
        if isPluginInstalled('FragMutti') and config.plugins.EtPortal.fragmutti.value:
            piclist.append(('fragmutti.png', _('Frag - Mutti')))
        if isPluginInstalled('KodiDirect') and config.plugins.EtPortal.kodi.value:
            piclist.append(('kodi.png', _('KODI Direct')))
        if isPluginInstalled('MovieArchiver') and config.plugins.EtPortal.moviearchiver.value:
            piclist.append(('moviearchiver.png', _('Movie Archiver')))
        if isPluginInstalled('YahooWeather') and config.plugins.EtPortal.yahooweather.value:
            piclist.append(('yahooweather.png', _('Yahoo Weather')))
        if isPluginInstalled('TSTube') and config.plugins.EtPortal.tstube.value:
            piclist.append(('youtube.png', _('TS Tube')))
        if isPluginInstalled('openATVreader') and config.plugins.EtPortal.atvreader.value:
            piclist.append(('atvreader.png', _('OpenATV Forum Reader ')))
			
        posX = 0
        hOffset = BORDER_OFFSET_SIZE
        for x in range(NUMBER_OF_PICTURES):
            if posX == 0 or posX == 6:
                tmpVoffset = 30
                tmpSize = IMAGE_SIZE_XXS
            elif posX == 1 or posX == 5:
                tmpVoffset = 20
                tmpSize = IMAGE_SIZE_XS
            elif posX == 2 or posX == 4:
                tmpVoffset = 10
                tmpSize = IMAGE_SIZE_S
            elif posX == 3:
                tmpVoffset = 0
                tmpSize = IMAGE_SIZE
            skincontent += '<widget name="thumb' + str(x) + '" position="' + str(hOffset) + ',' + str(tmpVoffset) + '" size="' + str(tmpSize) + ',' + str(tmpSize) + '" zPosition="2" transparent="1" alphatest="on" />'
            posX += 1
            if posX == 1:
                hOffset += IMAGE_SIZE_XXS + IMAGE_SPACE
            elif posX == 2 or posX == 6:
                hOffset += IMAGE_SIZE_XS + IMAGE_SPACE
            elif posX == 3 or posX == 5:
                hOffset += IMAGE_SIZE_S + IMAGE_SPACE
            elif posX == 4:
                hOffset += IMAGE_SIZE + IMAGE_SPACE

        if config.plugins.EtPortal.color.value == 'ice_HD':
            self.skin = '<screen position="0,0" size="1280,720" flags="wfNoBorder" backgroundColor="transparent" >'
            posX = 0
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/iceskin/icebar.png" position="0,0" size="1280,720" zPosition="0" transparent="1" alphatest="on" />'
            self.skin += '<widget source="label" render="Label" position="0,675" shadowColor="#000000" shadowOffset="1,1" size="1280,40" halign="center" font="Regular;30" zPosition="2" backgroundColor="#00000000" transparent="1" noWrap="1" foregroundColor="#1e90ff" />'
            self.skin += '<widget name="thumb0" position="100,545" size="170,170" zPosition="5" alphatest="on" transparent="1" />'
            self.skin += '<widget name="thumb1" position="257,545" size="170,170" zPosition="5" alphatest="on" transparent="1" />'
            self.skin += '<widget name="thumb2" position="414,536" size="170,170" zPosition="5" alphatest="on" transparent="1" />'
            self.skin += '<widget name="thumb3" position="570,520" size="170,170" zPosition="8" alphatest="on" transparent="1" />'
            self.skin += '<widget name="thumb4" position="728,536" size="170,170" zPosition="5" alphatest="on" transparent="1" />'
            self.skin += '<widget name="thumb5" position="886,545" size="170,170" zPosition="5" alphatest="on" transparent="1" />'
            self.skin += '<widget name="thumb6" position="1047,557" size="170,170" zPosition="5" alphatest="on" transparent="1" />'
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/pics/sel.png" position="562,520" size="150,130" zPosition="9" transparent="1" alphatest="on" />'
            self.skin += '<widget name="frame0" position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/iceskin/float0.png" zPosition="3" alphatest="on" />'
            self.skin += '<widget name="frame1" position="0,-720" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/iceskin/float1.png" zPosition="3" alphatest="on" />'
            self.skin += '</screen>'
        
        elif config.plugins.EtPortal.color.value == 'black_HD':
            self.skin = '<screen position="0,e-200" size="e-0,200" flags="wfNoBorder" backgroundColor="transparent" >'
            posX = 0
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/pics/sel.png" position="562,0" size="150,130" zPosition="2" transparent="1" alphatest="blend" />'
            self.skin += '<eLabel position="0,75" zPosition="0" size="e-0,e-90" backgroundColor="' + self.color + '" />' + skincontent
            self.skin += '<widget source="label" render="Label" position="0,148" size="e-0,40" halign="center" font="Regular;30" zPosition="2" backgroundColor="#00000000" transparent="1" noWrap="1" foregroundColor="' + self.textcolor + '" />'
            self.skin += '</screen>'
        
        elif config.plugins.EtPortal.color.value == 'SkinColor_HD':
            self.skin = '<screen position="0,e-200" size="e-0,200" flags="wfNoBorder" backgroundColor="transparent" >'
            posX = 0
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/pics/sel.png" position="562,0" size="150,130" zPosition="2" transparent="1" alphatest="blend" />'
            self.skin += '<eLabel position="0,75" zPosition="0" size="e-0,e-90" />' + skincontent
            self.skin += '<widget source="label" render="Label" position="0,148" size="e-0,40" halign="center" font="Regular;30" zPosition="2" backgroundColor="#00000000" transparent="1" noWrap="1" foregroundColor="' + self.textcolor + '" />'
            self.skin += '</screen>'
		
        elif config.plugins.EtPortal.color.value == 'Nobile_HD':
            self.skin = '<screen position="0,0" size="1280,720" flags="wfNoBorder" backgroundColor="transparent" >'
            posX = 0
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/NobileSkin/bar.png" position="0,0" size="1280,720" zPosition="0" transparent="1" alphatest="on" />'
            self.skin += '<widget source="label" render="Label" position="455,678" shadowColor="#000000" shadowOffset="1,1" size="360,40" halign="center" font="Regular;22" zPosition="2" backgroundColor="#00000000" transparent="1" noWrap="1" foregroundColor="#ffffff" />'
            self.skin += '<widget name="thumb0" position="100,557" size="170,170" zPosition="5" alphatest="on" backgroundColor="#d4d4d4" transparent="1" />'
            self.skin += '<widget name="thumb1" position="257,545" size="170,170" zPosition="5" alphatest="on" backgroundColor="#d4d4d4" transparent="1" />'
            self.skin += '<widget name="thumb2" position="414,536" size="170,170" zPosition="5" alphatest="on" backgroundColor="#d4d4d4" transparent="1" />'
            self.skin += '<widget name="thumb3" position="570,520" size="170,170" zPosition="8" alphatest="on" backgroundColor="#d4d4d4" transparent="1" />'
            self.skin += '<widget name="thumb4" position="728,536" size="170,170" zPosition="5" alphatest="on" backgroundColor="#d4d4d4" transparent="1" />'
            self.skin += '<widget name="thumb5" position="886,545" size="170,170" zPosition="5" alphatest="on" backgroundColor="#d4d4d4" transparent="1" />'
            self.skin += '<widget name="thumb6" position="1047,557" size="170,170" zPosition="5" alphatest="on" backgroundColor="#d4d4d4" transparent="1" />'
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/NobileSkin/sel.png" position="560,520" size="150,130" zPosition="9" transparent="1" alphatest="on" />'            
            self.skin += '</screen>'

        elif config.plugins.EtPortal.color.value == 'Xion_FullHD':
            self.skin = '<screen position="0,0" size="1920,1080" flags="wfNoBorder" backgroundColor="transparent" >'
            posX = 0
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/Xion/barhd.png" position="0,820" size="1920,1080" zPosition="0" transparent="1" alphatest="on" />'
            self.skin += '<widget source="label" render="Label" position="751,980" size="456,51" halign="center" font="Regular; 35" zPosition="2" backgroundColor="XionBackground" transparent="1" noWrap="1" foregroundColor="XionFont2" />'
            self.skin += '<widget name="thumb0" position="420,879" size="128,128" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb1" position="585,859" size="128,128" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb2" position="750,840" size="128,128" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb3" position="913,827" size="128,128" zPosition="8" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb4" position="1077,840" size="128,128" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb5" position="1242,859" size="128,128" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb6" position="1404,879" size="128,128" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/Xion/sel.png" position="902,826" size="150,150" zPosition="9" transparent="1" alphatest="on" />'            
            self.skin += '</screen>'

        elif config.plugins.EtPortal.color.value == 'Xion_HD':
            self.skin = '<screen position="0,0" size="1280,720" flags="wfNoBorder" backgroundColor="transparent" >'
            posX = 0
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/Xion/bar.png" position="0,520" size="1280,720" zPosition="0" transparent="1" alphatest="on" />'
            self.skin += '<widget source="label" render="Label" position="455,678" size="360,40" halign="center" font="Regular; 25" zPosition="2" backgroundColor="XionBackground" transparent="1" noWrap="1" foregroundColor="XionFont2" />'
            self.skin += '<widget name="thumb0" position="100,557" size="170,170" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb1" position="257,545" size="170,170" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb2" position="414,536" size="170,170" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb3" position="570,520" size="170,170" zPosition="8" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb4" position="728,536" size="170,170" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb5" position="886,545" size="170,170" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<widget name="thumb6" position="1047,557" size="170,170" zPosition="5" alphatest="on" backgroundColor="XionBackground" transparent="1" />'
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/Xion/sel.png" position="560,520" size="150,130" zPosition="9" transparent="1" alphatest="on" />'            
            self.skin += '</screen>'
            
        elif config.plugins.EtPortal.color.value == 'Metrix_FullHD':
            self.skin = '<screen position="0,0" size="1920,1080" flags="wfNoBorder" backgroundColor="transparent" >'
            posX = 0
            self.skin += '<eLabel position="0,900" size="1920,140" zPosition="0" backgroundColor="#40000000" />'
            self.skin += '<widget source="label" render="Label" position="751,980" size="456,51" halign="center" font="Regular; 29" zPosition="2" backgroundColor="#40000000" transparent="1" noWrap="1" foregroundColor="#0070ad11" />'
            self.skin += '<widget name="thumb0" position="420,879" size="128,128" zPosition="5" alphatest="on" backgroundColor="#0070ad11" transparent="1" />'
            self.skin += '<widget name="thumb1" position="585,859" size="128,128" zPosition="5" alphatest="on" backgroundColor="#40000000" transparent="1" />'
            self.skin += '<widget name="thumb2" position="750,840" size="128,128" zPosition="5" alphatest="on" backgroundColor="#40000000" transparent="1" />'
            self.skin += '<widget name="thumb3" position="913,827" size="128,128" zPosition="8" alphatest="on" backgroundColor="#40000000" transparent="1" />'
            self.skin += '<widget name="thumb4" position="1077,840" size="128,128" zPosition="5" alphatest="on" backgroundColor="#40000000" transparent="1" />'
            self.skin += '<widget name="thumb5" position="1242,859" size="128,128" zPosition="5" alphatest="on" backgroundColor="#40000000" transparent="1" />'
            self.skin += '<widget name="thumb6" position="1404,879" size="128,128" zPosition="5" alphatest="on" backgroundColor="#40000000" transparent="1" />'
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/pics/sel.png" position="902,826" size="150,150" zPosition="9" transparent="1" alphatest="on" />'            
            self.skin += '</screen>'
            
        Screen.__init__(self, session)
        self["actions"] = ActionMap(["MoviePlayerActions", "OkCancelActions", "DirectionActions", "EtPortalActions", "WizardActions", "NumberActions", "EPGSelectActions"],
		{
			"cancel": self.keyExit,
                        "ok": self.keyOk,
			"left": self.keyLeft,
			"right": self.keyRight,
			"up": self.keyPageUp,
			"menu": self.keyMenu,
			"down": self.keyPageDown,
			"info": self.keyGet,
			"mark_button": self.keyExit,
		}, -1)
		
        for x in range(NUMBER_OF_PICTURES):
            self['thumb' + str(x)] = Pixmap()

        self['label'] = StaticText()
        self.Thumbnaillist = []
        self.filelist = []
        self.isWorking = False
        index = 0
        framePos = 0
        Page = 0
        for x in piclist:
            self.filelist.append((index, SHARED_DIR_PATH + x[0], x[1]))
            index += 1
            framePos += 1

        self.maxentry = len(self.filelist)-1        
        if config.plugins.EtPortal.rememberposition.value:
            global global_index
            self.index = global_index
        else:
            self.index = 0
            
        self.picload = ePicLoad()
        self.picload.PictureData.get().append(self.showPic)
        self.onLayoutFinish.append(self.setPicloadConf)
        self.ThumbTimer = eTimer()
        self.ThumbTimer.callback.append(self.showPic)

        self['frame0'] = MovingPixmap()
        self['frame1'] = MovingPixmap()
        self.pos2 = []
        ict = 0
        j = -720
        while ict < 481:
            i1 = 0
            j1 = j
            self.pos2.append([i1, j1])
            j = j + 3
            ict = ict + 1

        self.index0 = -1
        self.index1 = 239
        self.updateTimer = eTimer()
        self.updateTimer.callback.append(self.updateStatus)
        self.updateTimer.start(128)
        self.updateStatus()
        self.onLayoutFinish.append(self.newPage)

    def updateStatus(self):
        self.index0 = self.index0 + 1
        self.index1 = self.index1 + 1
        self.paintFrame2()

    def paintFrame2(self):
        if self.index1 == 480:
            self.index1 = 0
        if self.index0 == 480:
            self.index0 = 0
        ipos = self.pos2[self.index0]
        ipos1 = self.pos2[self.index1]
        self['frame0'].moveTo(ipos[0], ipos[1], 1)
        self['frame1'].moveTo(ipos1[0], ipos1[1], 1)
        self['frame0'].startMoving()
        self['frame1'].startMoving()

    def setPicloadConf(self):
        sc = AVSwitch().getFramebufferScale()
        self.picload.setPara([IMAGE_SIZE_XXS, IMAGE_SIZE_XXS, sc[0], sc[1], False, 1, self.color])

    def newPage(self):
        self.Thumbnaillist = []
        for x in range(NUMBER_OF_PICTURES):
            self['thumb' + str(x)].hide()

        idx = 0
        offset = 0
        while idx < NUMBER_OF_PICTURES:
            if len(self.filelist) <= self.index + idx:
                try:
                    self.Thumbnaillist.append([0, idx, self.filelist[offset][1], self.filelist[offset][2]])
                    offset += 1
                except:
                    pass
            else:
                self.Thumbnaillist.append([0, idx, self.filelist[offset + self.index][1], self.filelist[offset + self.index][2]])
                offset += 1
                if len(self.filelist) == self.index + offset:
                    offset = 0
            idx += 1

        self.isWorking = True
        self.showPic()

    def showPic(self, picInfo=""):
        cnt = 0
        for x in range(NUMBER_OF_PICTURES):
            cnt += 1
            try:
                if self.Thumbnaillist[x][0] == 0:
                    if self.picload.getThumbnail(self.Thumbnaillist[x][2]) == 1:
                        self.ThumbTimer.start(500, True)
                    else:
                        self.Thumbnaillist[x][0] = 1
                    break
                elif self.Thumbnaillist[x][0] == 1:
                    self.Thumbnaillist[x][0] = 2
                    ptr = self.picload.getData()
                    if ptr != None:
                        self["thumb" + str(self.Thumbnaillist[x][1])].instance.setPixmap(ptr.__deref__())
                        sc = AVSwitch().getFramebufferScale()
                        tmp = self.Thumbnaillist[x][1] + 1
                        if  tmp == 3:
                            self.picload.setPara([IMAGE_SIZE, IMAGE_SIZE, sc[0], sc[1], False, 1, self.color])
                    
                        elif tmp == 2 or tmp == 4:
                            self.picload.setPara([IMAGE_SIZE_S, IMAGE_SIZE_S, sc[0], sc[1], False, 1, self.color])
                    
                        elif tmp == 1 or tmp == 5:
                            self.picload.setPara([IMAGE_SIZE_XS, IMAGE_SIZE_XS, sc[0], sc[1], False, 1, self.color])
                    
                        else:
                            self.picload.setPara([IMAGE_SIZE_XXS, IMAGE_SIZE_XXS, sc[0], sc[1], False, 1, self.color])
                    
                        self["thumb" + str(self.Thumbnaillist[x][1])].show()

                elif self.Thumbnaillist[x][0] == 2:
                    if cnt == 6:
                        self["label"].setText(self.Thumbnaillist[3][3])
                        writeToVFD(self.Thumbnaillist[3][3])
                        self.isWorking = False
            except:
                    message = _("EtPortal:\n\nPlease select at least 7 Extensions in (EtPortal Setup)")
                    self.session.openWithCallback(self.close, MessageBox, message, MessageBox.TYPE_INFO, timeout = 30)

    def keyPageDown(self):
        if self.isWorking:
            return
        self.index -= 7
        if self.index < 0:
            self.index = self.maxentry
        self.newPage()
    
    def keyPageUp(self):
        if self.isWorking:
            return
        self.index += 7
        if self.index > self.maxentry:
            self.index = 0
        self.newPage()
        
    def keyLeft(self):
        if self.isWorking:
            return
        self.index -= 1
        if self.index < 0:
            self.index = self.maxentry
        self.newPage()

    def keyMenu(self):
        self.session.open(EtPortalSetupScreen)

    def keyRight(self):
        if self.isWorking:
            return
        self.index += 1
        if self.index > self.maxentry:
            self.index = 0
        self.newPage()

    def keyOk(self):
        global didOpen
        if 'timer.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.showtimericon.value:
                from Screens.TimerEdit import TimerEditList
                self.session.open(TimerEditList)
        elif 'shutdown.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.shutdown.value:
                from Screens.Menu import MainMenu
                import xml.etree.cElementTree
                menu = xml.etree.cElementTree.parse(SHARED_DIR_PATH + 'shutdown.xml').getroot()
                self.session.open(MainMenu, menu)
        elif 'information.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.systeminfo.value:
                from Screens.Menu import MainMenu
                import xml.etree.cElementTree
                menu = xml.etree.cElementTree.parse(SHARED_DIR_PATH + 'information.xml').getroot()
                self.session.open(MainMenu, menu)
        elif 'dreamexplorer.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('DreamExplorer'):
                from Plugins.Extensions.DreamExplorer.plugin import DreamExplorerII
                self.session.open(DreamExplorerII)
        elif 'movie_player.png' in self.Thumbnaillist[3][2]:
            from Screens.InfoBar import InfoBar
            if InfoBar and InfoBar.instance:
                InfoBar.showMovies(InfoBar.instance)
        elif 'media_player.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('MediaPlayer'):
                from Plugins.Extensions.MediaPlayer.plugin import MediaPlayer
                self.session.open(MediaPlayer)
        elif 'dvd_player.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('DVDPlayer'):
                from Plugins.Extensions.DVDPlayer.plugin import DVDPlayer
                self.session.open(DVDPlayer)
        elif 'kodi.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('KodiDirect'):
                # from Plugins.Extensions.KodiDirect.plugin import *
                from Components.PluginComponent import plugins
                plugin = _('KodiDirect')
                for p in plugins.getPlugins(where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU]):
                    if 'KodiDirect' == str(p.name):
                        plugin = p
                if plugin is not None:
                    plugin(session=self.session)
        elif 'dreamplex.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.dreamplex.value:
                from Plugins.Extensions.DreamPlex.plugin import DPS_MainMenu
                from Components.PluginComponent import plugins
                self.session.open(DPS_MainMenu)
        elif 'emc.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.emc.value:
                from Plugins.Extensions.EnhancedMovieCenter.plugin import showMoviesNew
                from Components.PluginComponent import plugins
                showMoviesNew()
        elif 'picture_player.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('PicturePlayer' ,'ui'):
                from Plugins.Extensions.PicturePlayer.ui import picshow
                self.session.open(picshow)
        elif 'network.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('NetworkBrowser', 'NetworkBrowser'):
                from Plugins.SystemPlugins.NetworkBrowser.plugin import NetworkBrowser
                iface = None
                self.session.open(NetworkBrowser, iface, plugin_path)
        elif 'youtube.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('TSTube'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                #from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'TSTube' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'atvreader.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('openATVreader'):
                from Plugins.Extensions.openATVreader.plugin import openatv
                self.session.open(openatv.OPENA_TV_HauptScreen)
        elif 'iptv.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('IPTV-List-Updater'):
                _temp = __import__('Plugins.Extensions.IPTV-List-Updater.plugin', globals(), locals(), ['Start'], -1)
                Start = _temp.Start
                self.session.open(Start)
        elif 'tanken.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('clever-tanken'):
                _temp = __import__('Plugins.Extensions.clever-tanken.plugin', globals(), locals(), ['clevertankenMain'], -1)
                clevertankenMain = _temp.clevertankenMain
                self.session.open(clevertankenMain)
        elif 'tvspielfilm.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('TVSpielfilm'):
                from Plugins.Extensions.TVSpielfilm.plugin import tvMain
                self.session.open(tvMain)
        elif 'chefkoch.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('Chefkoch'):
                from Plugins.Extensions.Chefkoch.plugin import ChefkochMain
                self.session.open(ChefkochMain)
        elif 'xtrend.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('OpenXtaReader'):
                from Plugins.Extensions.OpenXtaReader.plugin import OpenXtaMain
                self.session.open(OpenXtaMain)
        elif 'merlinmusic.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.merlinmusic.value:
                from Plugins.Extensions.MerlinMusicPlayer.plugin import MerlinMusicPlayerFileList
                servicelist = None
                self.session.open(MerlinMusicPlayerFileList, servicelist)
        elif 'foreca.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('Foreca'):
                #from Plugins.Extensions.Foreca.plugin import *
                from Components.PluginComponent import plugins
                plugin = _("Foreca Wettervorhersage")
                for p in plugins.getPlugins(where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU]):
                    if 'Foreca Wettervorhersage' == str(p.name):
                        plugin = p
                if plugin is not None:
                    plugin(session=self.session)
        #elif 'youporn.png' in self.Thumbnaillist[3][2]:
        #    password = '/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/adultpassword'
        #    if fileExists(password):
        #        c = open(password, 'r')
        #        for line in c:
        #            self.passw = line
        #        c.close()
        #    if config.plugins.EtPortal.adult.value == self.passw:
        #        from Plugins.Extensions.YouPorn.plugin import *
        #        self.session.open(youpornMain, True)
        #    else:
        #        self.session.open(MessageBox, _('wrong password!'), MessageBox.TYPE_INFO, timeout=8)
        elif 'digitalfernsehen.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.digitalfernsehen.value:
                from Plugins.Extensions.DIGITALfernsehen.plugin import digitalTVMain
                self.session.open(digitalTVMain)
        elif 'bluray.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.bluray.value:
                if config.plugins.EtPortal.blurayconfig.value == 'List':
                    _temp = __import__('Plugins.Extensions.Blu-ray.plugin', globals(), locals(), ['blurayMainList'], -1)
                    blurayMainList = _temp.blurayMainList
                    self.session.open(blurayMainList)
                elif config.plugins.EtPortal.blurayconfig.value == 'Cover':
                    _temp = __import__('Plugins.Extensions.Blu-ray.plugin', globals(), locals(), ['blurayMainCover'], -1)
                    blurayMainCover = _temp.blurayMainCover
                    self.session.open(blurayMainCover)
                elif config.plugins.EtPortal.blurayconfig.value == 'Cover_Full':
                    _temp = __import__('Plugins.Extensions.Blu-ray.plugin', globals(), locals(), ['blurayMainCoverFull'], -1)
                    blurayMainCoverFull = _temp.blurayMainCoverFull
                    self.session.open(blurayMainCoverFull)
        elif 'bild.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.bild.value:
                from Plugins.Extensions.BILDOnline.plugin import bildMain
                self.session.open(bildMain)
        elif 'kino.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.kinode.value:
                from Plugins.Extensions.KINOde.plugin import kinoMain
                self.session.open(kinoMain)
        elif 'spiegel.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.spiegel.value:
                from Plugins.Extensions.SPIEGELOnline.plugin import spiegelMain
                self.session.open(spiegelMain)
        elif 'focus.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.focus.value:
                from Plugins.Extensions.FOCUSOnline.plugin import focusMain
                self.session.open(focusMain)
        elif 'wiki.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.wiki.value:
                from Plugins.Extensions.Wikipedia.plugin import wikiMain
                self.session.open(wikiMain)
        elif 'kicker.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('kicker'):
                from Plugins.Extensions.kicker.plugin import kickerMain
                self.session.open(kickerMain)
        elif 'kickerticker.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('kicker'):
                from Plugins.Extensions.kicker.plugin import tickerMain
                self.session.open(tickerMain)
        elif 'verkehrsinfo.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.verkehrsinfo.value:
                from Plugins.Extensions.verkehrsinfo.plugin import verkehrsinfoMain
                self.session.open(verkehrsinfoMain)
        elif 'muzutv.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.muzutv.value:
                from Plugins.Extensions.MUZUtv.plugin import muzuMain
                self.session.open(muzuMain)
        elif 'facebook.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.facebook.value:
                from Plugins.Extensions.Facebook.plugin import loginCheck
                self.session.open(loginCheck)
        elif 'mediaportal.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('MediaPortal'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                # from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'MediaPortal' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'skyrecorder.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('skyrecorder'):
                from Plugins.Extensions.skyrecorder.plugin import SkyRecorderMainScreen
                self.session.open(SkyRecorderMainScreen)
        elif 'tvcharts.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('TVCharts'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                #from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'TV Charts' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'mp3browser.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('MP3Browser'):
                #from Plugins.Extensions.MP3Browser.plugin import *
                from Components.PluginComponent import plugins
                plugin = _('MP3 Browser')
                for p in plugins.getPlugins(where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU]):
                    if 'MP3 Browser' == str(p.name):
                        plugin = p
                if plugin is not None:
                    plugin(session=self.session)
        elif 'moviebrowser.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('MovieBrowser'):
                #from Plugins.Extensions.MovieBrowser.plugin import *
                from Components.PluginComponent import plugins
                plugin = _('Movie Browser')
                for p in plugins.getPlugins(where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU]):
                    if 'Movie Browser' == str(p.name):
                        plugin = p
                if plugin is not None:
                    plugin(session=self.session)
        elif 'valerie.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('ProjectValerie'):
                from Plugins.Extensions.ProjectValerie.plugin import PVMC_MainMenu
                self.session.open(PVMC_MainMenu)
        elif 'webradiofs.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('webradioFS'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                # from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'webradioFS' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'yamp.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('YampMusicPlayer'):
                from Plugins.Extensions.YampMusicPlayer.plugin import Yamp
                reload(Yamp)
                self.session.open(Yamp.YampScreen)
        elif 'shoutcast.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('SHOUTcast'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                # from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'SHOUTcast' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'tunein.png' in self.Thumbnaillist[3][2]:            
            if isPluginInstalled('OpenOpera'):
                from Plugins.Extensions.OpenOpera.plugin import browserinstance, BrowserRemoteControl
            elif isPluginInstalled('NXHbbTV'):
                from Plugins.Extensions.NXHbbTV.plugin import browserinstance, BrowserRemoteControl
            browserinstance.start()
            if browserinstance.is_browser_running() is True:
                url = 'http://ce.radiotime.com'
                browserinstance.showSendUrl(url, 1) 
                self.session.open(BrowserRemoteControl, True, False)
        elif 'wikitv.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('OpenOpera'):
                from Plugins.Extensions.OpenOpera.plugin import browserinstance, BrowserRemoteControl
            elif isPluginInstalled('NXHbbTV'):
                from Plugins.Extensions.NXHbbTV.plugin import browserinstance, BrowserRemoteControl
            browserinstance.start()
            if browserinstance.is_browser_running() is True:
                url = 'http://portal.primatv.de/wikitv'
                browserinstance.showSendUrl(url, 1) 
                self.session.open(BrowserRemoteControl, True, False)
        elif 'hbbig.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('OpenOpera'):
                from Plugins.Extensions.OpenOpera.plugin import browserinstance, BrowserRemoteControl
            elif isPluginInstalled('NXHbbTV'):
                from Plugins.Extensions.NXHbbTV.plugin import browserinstance, BrowserRemoteControl
            browserinstance.start()
            if browserinstance.is_browser_running() is True:
                url = 'http://hbbig.com'
                browserinstance.showSendUrl(url, 1) 
                self.session.open(BrowserRemoteControl, True, False)
        elif 'watchmi.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('OpenOpera'):
                from Plugins.Extensions.OpenOpera.plugin import browserinstance, BrowserRemoteControl
            elif isPluginInstalled('NXHbbTV'):
                from Plugins.Extensions.NXHbbTV.plugin import browserinstance, BrowserRemoteControl
            browserinstance.start()
            if browserinstance.is_browser_running() is True:
                url = 'http://watchmi-smarttv.api.watchmi.tv/app/watchmi-smarttv/cehtml.cehtml'
                browserinstance.showSendUrl(url, 1) 
                self.session.open(BrowserRemoteControl, True, False)
        elif 'ardhbbtv.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('OpenOpera'):
                from Plugins.Extensions.OpenOpera.plugin import browserinstance, BrowserRemoteControl
            elif isPluginInstalled('NXHbbTV'):
                from Plugins.Extensions.NXHbbTV.plugin import browserinstance, BrowserRemoteControl
            browserinstance.start()
            if browserinstance.is_browser_running() is True:
                url = 'http://web.ard.de/hbbtv-portal/index.php'
                browserinstance.showSendUrl(url, 1) 
                self.session.open(BrowserRemoteControl, True, False)
        elif 'turkvod.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('TURKvod'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                #rom Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'TURKvod' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'greekstreamtv.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('GreekStreamTV'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                # from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'GreekStreamTV' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'opera.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('OpenOpera'):
                from Plugins.Extensions.OpenOpera.plugin import browserinstance, BrowserRemoteControl
            elif isPluginInstalled('NXHbbTV'):
                from Plugins.Extensions.NXHbbTV.plugin import browserinstance, BrowserRemoteControl
            browserinstance.start()
            self.session.open(BrowserRemoteControl, False, True)
        elif 'weblinks.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('Weblinks'):
                from Plugins.Extensions.Weblinks.plugin import WebLinksSelectMenu
                self.session.open(WebLinksSelectMenu)
        elif 'extensions_plugins.png' in self.Thumbnaillist[3][2]:
            from Screens.InfoBar import InfoBar
            if InfoBar and InfoBar.instance:
                InfoBar.showExtensionSelection(InfoBar.instance)
        elif 'plugins.png' in self.Thumbnaillist[3][2]:
            from Screens.PluginBrowser import PluginBrowser
            self.session.open(PluginBrowser)
        elif 'powertimer.png' in self.Thumbnaillist[3][2]:
            #if fileExists('/usr/lib/enigma2/python/Screens/PowerTimerEdit.pyo'):
            from Screens.Menu import MainMenu
            import xml.etree.cElementTree
            menu = xml.etree.cElementTree.parse(SHARED_DIR_PATH + 'powertimer.xml').getroot()
            self.session.open(MainMenu, menu)
        elif 'mediainfo.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('MediaInfo'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                #from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'MediaInfo' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'downloadcenter.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('downloadcenter'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                # from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'DownloadCenter' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'fragmutti.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('FragMutti'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                # from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'Frag Mutti' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'moviearchiver.png' in self.Thumbnaillist[3][2]:
            if isPluginInstalled('MovieArchiver'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                # from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'MovieArchiver' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'yahooweather.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.yahooweather.value:
                from Plugins.Extensions.YahooWeather.plugin import MeteoMain
                self.session.open(MeteoMain)
        if config.plugins.EtPortal.finalexit.value:
            if 'movie_player.png' in self.Thumbnaillist[3][2] or 'mediaportal.png' in self.Thumbnaillist[3][2]:
                if config.plugins.EtPortal.finalexit.value == 'True':
                    self.close(False)
            else:
                self.close(True)

    def keyExit(self):
        global global_index
        if config.plugins.EtPortal.rememberposition.value:
            global_index = self.index
        self.close()

    def keyGet(self):
        if config.plugins.EtPortal.Get.value:
            if 'wiki.png' in self.Thumbnaillist[3][2]:
                if config.plugins.EtPortal.wiki.value:
                    from Plugins.Extensions.Wikipedia.plugin import wikiEvent
                    self.session.open(wikiEvent)
            elif 'tvspielfilm.png' in self.Thumbnaillist[3][2]:
                if isPluginInstalled('TVSpielfilm'):
                    from Plugins.Extensions.TVSpielfilm.plugin import tvEvent
                    self.session.open(tvEvent)
            elif 'moviebrowser.png' in self.Thumbnaillist[3][2]:
                if isPluginInstalled('MovieBrowser'):
                    from Plugins.Extensions.MovieBrowser.plugin import movieBrowserPosterwall
                    self.session.open(movieBrowserPosterwall, 0, config.plugins.moviebrowser.filter.value, config.plugins.moviebrowser.filter.value)

class EtPortalSetupScreen(Screen, ConfigListScreen):
    if skin_w  == 1920:
        skin = """
	    <screen position="center,center" size="900,850" title="EtPortal %s %s">
		    <widget name="config" position="25,25" font="Regular;30" itemHeight="40" scrollbarMode="showOnDemand" size="850,690" />
		    <eLabel position="25,771" size="10,60" zPosition="1" backgroundColor="#00f23d21" />
		    <widget source="key_red" render="Label" position="48,771" size="260,60" zPosition="1" font="Regular;36" valign="center" halign="left" foregroundColor="#ffffff" transparent="1" />
		    <eLabel position="325,771" size="10,60" zPosition="1" backgroundColor="#00389416" />
		    <widget source="key_green" render="Label" position="348,771" size="260,60" zPosition="1" font="Regular;36" valign="center" halign="left" foregroundColor="#ffffff" transparent="1" />
	    </screen>""" % (EtPortalVersion, _("Setup"))
    else:
        skin = """
	    <screen position="c-300,c-250" size="600,500" title="EtPortal %s %s">
		    <widget name="config" position="25,25" scrollbarMode="showOnDemand" size="550,400" />
		    <ePixmap pixmap="skin_default/buttons/red.png" position="20,e-45" size="140,40" alphatest="on" />
		    <ePixmap pixmap="skin_default/buttons/green.png" position="160,e-45" size="140,40" alphatest="on" />
		    <widget source="key_red" render="Label" position="20,e-45" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />
		    <widget source="key_green" render="Label" position="160,e-45" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />
	    </screen>""" % (EtPortalVersion, _("Setup"))
	    
    def __init__(self, session):
        self.skin = EtPortalSetupScreen.skin
        Screen.__init__(self, session)
        self['key_red'] = StaticText(_('Cancel'))
        self['key_green'] = StaticText(_('OK'))
        self['actions'] = ActionMap(['SetupActions', 'ColorActions', 'EPGSelectActions', 'NumberActions'], 
        {'ok': self.keyGo,
         'left': self.keyLeft,
         'right': self.keyRight,
         'save': self.keyGo,
         'cancel': self.keyCancel,
         'green': self.keyGo,
         'red': self.keyCancel,
         'blue': self.keyGet,
         'nextBouquet': self.up,
         'prevBouquet': self.down}, -2)
         
        self.list = []
        ConfigListScreen.__init__(self, self.list, session=self.session)
        self.list.append(getConfigListEntry(_('Select Style / Backround color'), config.plugins.EtPortal.color))
        self.list.append(getConfigListEntry(_('Exit portal after selecting an option'), config.plugins.EtPortal.finalexit))
        self.list.append(getConfigListEntry(_('Remember last menu position'), config.plugins.EtPortal.rememberposition))
        self.list.append(getConfigListEntry(_('Enable Timer and Mark or Portal Button'), config.plugins.EtPortal.enablemarkbutton))
        self.list.append(getConfigListEntry(_('Show Selection in VFD-Display'), config.plugins.EtPortal.vfd))
        self.list.append(getConfigListEntry(_(' '), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_(' '), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Show following Plugins/Extensions:'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_(' '), config.plugins.EtPortal.none))
        
        if isPluginInstalled('openATVreader'):
            self.list.append(getConfigListEntry(_('OpenATV Forum Reader'), config.plugins.EtPortal.atvreader))
        else:
            self.list.append(getConfigListEntry(_('OpenATV Forum Reader'), config.plugins.EtPortal.none))
        if isPluginInstalled('OpenOpera') or isPluginInstalled('NXHbbTV'):
            self.list.append(getConfigListEntry(_('ARD HbbTV-Portal'), config.plugins.EtPortal.ardhbbtv))
        else:
            self.list.append(getConfigListEntry(_('ARD HbbTV-Portal'), config.plugins.EtPortal.none))
        if isPluginInstalled('BILDOnline'):
            self.list.append(getConfigListEntry(_('Bild.de'), config.plugins.EtPortal.bild))
        else:
            self.list.append(getConfigListEntry(_('Bild.de'), config.plugins.EtPortal.none))
        if isPluginInstalled('Blu-ray'):
            self.list.append(getConfigListEntry(_('BLURAY-DISC.de'), config.plugins.EtPortal.bluray))
            if config.plugins.EtPortal.bluray.value == True:
                self.list.append(getConfigListEntry(_('BLURAY-DISC.de      (Start)'), config.plugins.EtPortal.blurayconfig))
        else:
            self.list.append(getConfigListEntry(_('BLURAY-DISC.de'), config.plugins.EtPortal.none))
        if isPluginInstalled('Chefkoch'):
            self.list.append(getConfigListEntry(_('Chefkoch.de'), config.plugins.EtPortal.Chefkoch))
        else:
            self.list.append(getConfigListEntry(_('Chefkoch.de'), config.plugins.EtPortal.none))
        if isPluginInstalled('clever-tanken'):
            self.list.append(getConfigListEntry(_('clever-tanken.de'), config.plugins.EtPortal.tanken))
        else:
            self.list.append(getConfigListEntry(_('clever-tanken.de'), config.plugins.EtPortal.none))
        if isPluginInstalled('DIGITALfernsehen'):
            self.list.append(getConfigListEntry(_('DiGITAL fernsehen'), config.plugins.EtPortal.digitalfernsehen))
        else:
            self.list.append(getConfigListEntry(_('DiGITAL fernsehen'), config.plugins.EtPortal.none))
        if isPluginInstalled('downloadcenter'):
            self.list.append(getConfigListEntry(_('DownloadCenter'), config.plugins.EtPortal.downloadcenter))
        else:
            self.list.append(getConfigListEntry(_('DownloadCenter'), config.plugins.EtPortal.none))
        if isPluginInstalled('/usr/lib/enigma2/python/Plugins/Extensions/DVDPlayer/keymap.xml'):
            self.list.append(getConfigListEntry(_('DVD-Player'), config.plugins.EtPortal.dvd))
        else:
            self.list.append(getConfigListEntry(_('DVD-Player'), config.plugins.EtPortal.none))
        if isPluginInstalled('DreamExplorer'):
            self.list.append(getConfigListEntry(_('DreamExplorer'), config.plugins.EtPortal.dreamexplorer))
        else:
            self.list.append(getConfigListEntry(_('DreamExplorer'), config.plugins.EtPortal.none))
        if isPluginInstalled('DreamPlex'):
            self.list.append(getConfigListEntry(_('DreamPlex'), config.plugins.EtPortal.dreamplex))
        else:
            self.list.append(getConfigListEntry(_('DreamPlex'), config.plugins.EtPortal.none))
        if isPluginInstalled('EnhancedMovieCenter'):
            self.list.append(getConfigListEntry(_('EMC'), config.plugins.EtPortal.emc))
        else:
            self.list.append(getConfigListEntry(_('EMC'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Extension Plugins and applications'), config.plugins.EtPortal.extensions))
        if isPluginInstalled('Facebook'):
            self.list.append(getConfigListEntry(_('Facebook'), config.plugins.EtPortal.facebook))
        else:
            self.list.append(getConfigListEntry(_('Facebook'), config.plugins.EtPortal.none))
        if isPluginInstalled('FOCUSOnline'):
            self.list.append(getConfigListEntry(_('Focus ONLINE'), config.plugins.EtPortal.focus))
        else:
            self.list.append(getConfigListEntry(_('Focus ONLINE'), config.plugins.EtPortal.none))
        if isPluginInstalled('Foreca'):
            self.list.append(getConfigListEntry(_('Foreca'), config.plugins.EtPortal.foreca))
        else:
            self.list.append(getConfigListEntry(_('Foreca'), config.plugins.EtPortal.none))
        if isPluginInstalled('GreekStreamTV'):
            self.list.append(getConfigListEntry(_('GreekStreamTV'), config.plugins.EtPortal.greekstreamtv))
        else:
            self.list.append(getConfigListEntry(_('GreekStreamTV'), config.plugins.EtPortal.none))
        if isPluginInstalled('FragMutti'):
            self.list.append(getConfigListEntry(_('Frag - Mutti'), config.plugins.EtPortal.fragmutti))
        else:
            self.list.append(getConfigListEntry(_('Frag - Mutti'), config.plugins.EtPortal.none))
        if isPluginInstalled('OpenOpera') or isPluginInstalled('NXHbbTV'):
            self.list.append(getConfigListEntry(_('HBBig'), config.plugins.EtPortal.hbbig))
        else:
            self.list.append(getConfigListEntry(_('HBBig'), config.plugins.EtPortal.none))
        if isPluginInstalled('IPTV-List-Updater'):
            self.list.append(getConfigListEntry(_('IPTV-List Updater'), config.plugins.EtPortal.iptv))
        else:
            self.list.append(getConfigListEntry(_('IPTV-List Updater'), config.plugins.EtPortal.none))
        if isPluginInstalled('kicker'):
            self.list.append(getConfigListEntry(_('Kicker Online'), config.plugins.EtPortal.kicker))
        else:
            self.list.append(getConfigListEntry(_('Kicker Online'), config.plugins.EtPortal.none))
        if isPluginInstalled('kicker'):
            self.list.append(getConfigListEntry(_('Kicker Live-Ticker'), config.plugins.EtPortal.kickerticker))
        else:
            self.list.append(getConfigListEntry(_('Kicker Live-Ticker'), config.plugins.EtPortal.none))
        if isPluginInstalled('KINOde'):
            self.list.append(getConfigListEntry(_('Kino.de'), config.plugins.EtPortal.kinode))
        else:
            self.list.append(getConfigListEntry(_('Kino.de'), config.plugins.EtPortal.none))
        if isPluginInstalled('KodiDirect'):
            self.list.append(getConfigListEntry(_('KODI Direct'), config.plugins.EtPortal.kodi))
        else:
            self.list.append(getConfigListEntry(_('KODI Direct'), config.plugins.EtPortal.none))
        if isPluginInstalled('MediaInfo'):
            self.list.append(getConfigListEntry(_('MediaInfo'), config.plugins.EtPortal.mediainfo))
        else:
            self.list.append(getConfigListEntry(_('MediaInfo'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Media-Player'), config.plugins.EtPortal.media))
        if isPluginInstalled('MediaPortal'):
            self.list.append(getConfigListEntry(_('Media Portal'), config.plugins.EtPortal.mediaportal))
        else:
            self.list.append(getConfigListEntry(_('Media Portal'), config.plugins.EtPortal.none))
        if isPluginInstalled('MerlinMusicPlayer'):
            self.list.append(getConfigListEntry(_('Merlin-Music Player'), config.plugins.EtPortal.merlinmusic))
        else:
            self.list.append(getConfigListEntry(_('Merlin-Music Player'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Movielist'), config.plugins.EtPortal.movie))
        if isPluginInstalled('MovieArchiver'):
            self.list.append(getConfigListEntry(_('Movie Archiver'), config.plugins.EtPortal.moviearchiver))
        else:
            self.list.append(getConfigListEntry(_('Movie Archiver'), config.plugins.EtPortal.none))
        if isPluginInstalled('MovieBrowser'):
            self.list.append(getConfigListEntry(_('Movie-Browser'), config.plugins.EtPortal.moviebrowser))
        else:
            self.list.append(getConfigListEntry(_('Movie-Browser'), config.plugins.EtPortal.none))
        if isPluginInstalled('MP3Browser'):
            self.list.append(getConfigListEntry(_('mp3-Browser'), config.plugins.EtPortal.mp3browser))
        else:
            self.list.append(getConfigListEntry(_('mp3-Browser'), config.plugins.EtPortal.none))
        if isPluginInstalled('MUZUtv'):
            self.list.append(getConfigListEntry(_('MUZU.TV'), config.plugins.EtPortal.muzutv))
        else:
            self.list.append(getConfigListEntry(_('MUZU.TV'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/SystemPlugins/NetworkBrowser'):
            self.list.append(getConfigListEntry(_('Network Browser'), config.plugins.EtPortal.networkbrowser))
        else:
            self.list.append(getConfigListEntry(_('Network Browser'), config.plugins.EtPortal.none))
        if isPluginInstalled('OpenOpera') or isPluginInstalled('NXHbbTV'):
            self.list.append(getConfigListEntry(_('Opera'), config.plugins.EtPortal.operabrowser))
        else:
            self.list.append(getConfigListEntry(_('Opera'), config.plugins.EtPortal.none))
        if isPluginInstalled('PicturePlayer', 'ui'):
            self.list.append(getConfigListEntry(_('Picture Player'), config.plugins.EtPortal.picture))
        else:
            self.list.append(getConfigListEntry(_('Picture Player'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Plugin Browser'), config.plugins.EtPortal.pluginbrowser))
        #if fileExists('/usr/lib/enigma2/python/Screens/PowerTimerEdit.pyo'):
        self.list.append(getConfigListEntry(_('Power Timer'), config.plugins.EtPortal.powertimer))
        self.list.append(getConfigListEntry(_('Sleeptimer and power control'), config.plugins.EtPortal.shutdown))
        if isPluginInstalled('SHOUTcast'):
            self.list.append(getConfigListEntry(_('SHOUTcast'), config.plugins.EtPortal.shoutcast))
        else:
            self.list.append(getConfigListEntry(_('SHOUTcast'), config.plugins.EtPortal.none))
        if isPluginInstalled('skyrecorder'):
            self.list.append(getConfigListEntry(_('sky recorder'), config.plugins.EtPortal.skyrecorder))
        else:
            self.list.append(getConfigListEntry(_('sky recorder'), config.plugins.EtPortal.none))
        if isPluginInstalled('SPIEGELOnline'):
            self.list.append(getConfigListEntry(_('Spiegel ONLINE'), config.plugins.EtPortal.spiegel))
        else:
            self.list.append(getConfigListEntry(_('Spiegel ONLINE'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('System Information'), config.plugins.EtPortal.systeminfo))
        self.list.append(getConfigListEntry(_('Timer Option'), config.plugins.EtPortal.showtimericon))
        if isPluginInstalled('TSTube'):
            self.list.append(getConfigListEntry(_('TS Tube'), config.plugins.EtPortal.tstube))
        else:
            self.list.append(getConfigListEntry(_('TS Tube'), config.plugins.EtPortal.none))
        if isPluginInstalled('OpenOpera') or isPluginInstalled('NXHbbTV'):
            self.list.append(getConfigListEntry(_('tunein Radio'), config.plugins.EtPortal.tunein))
        else:
            self.list.append(getConfigListEntry(_('tunein Radio'), config.plugins.EtPortal.none))
        if isPluginInstalled('TURKvod'):
            self.list.append(getConfigListEntry(_('TURKvod IPTV'), config.plugins.EtPortal.turkvod))
        else:
            self.list.append(getConfigListEntry(_('TURKvod IPTV'), config.plugins.EtPortal.none))
        if isPluginInstalled('TVCharts'):
            self.list.append(getConfigListEntry(_('TV Charts'), config.plugins.EtPortal.tvcharts))
        else:
            self.list.append(getConfigListEntry(_('TV Charts'), config.plugins.EtPortal.none))
        if isPluginInstalled('TVSpielfilm'):
            self.list.append(getConfigListEntry(_('TVSpielfilm'), config.plugins.EtPortal.tvspielfilm))
        else:
            self.list.append(getConfigListEntry(_('TVSpielfilm'), config.plugins.EtPortal.none))
        if isPluginInstalled('ProjectValerie'):
            self.list.append(getConfigListEntry(_('Project-Valerie'), config.plugins.EtPortal.pvmc))
        else:
            self.list.append(getConfigListEntry(_('Project-Valerie'), config.plugins.EtPortal.none))
        if isPluginInstalled('verkehrsinfo'):
            self.list.append(getConfigListEntry(_('Verkehrsinfo.de'), config.plugins.EtPortal.verkehrsinfo))
        else:
            self.list.append(getConfigListEntry(_('Verkehrsinfo.de'), config.plugins.EtPortal.none))
        if isPluginInstalled('OpenOpera') or isPluginInstalled('NXHbbTV'):
            self.list.append(getConfigListEntry(_('watchmi'), config.plugins.EtPortal.watchmi))
        else:
            self.list.append(getConfigListEntry(_('watchmi'), config.plugins.EtPortal.none))
        if isPluginInstalled('Weblinks'):
            self.list.append(getConfigListEntry(_('WebLinks'), config.plugins.EtPortal.weblinks))
        else:
            self.list.append(getConfigListEntry(_('Weblinks'), config.plugins.EtPortal.none))
        if isPluginInstalled('webradioFS'):
            self.list.append(getConfigListEntry(_('WebRadio FS'), config.plugins.EtPortal.webradiofs))
        else:
            self.list.append(getConfigListEntry(_('WebRadio FS'), config.plugins.EtPortal.none))
        if isPluginInstalled('Wikipedia'):
            self.list.append(getConfigListEntry(_('Wikipedia'), config.plugins.EtPortal.wiki))
        else:
            self.list.append(getConfigListEntry(_('Wikipedia'), config.plugins.EtPortal.none))
        if isPluginInstalled('OpenOpera') or isPluginInstalled('NXHbbTV'):
            self.list.append(getConfigListEntry(_('Wiki TV'), config.plugins.EtPortal.wikitv))
        else:
            self.list.append(getConfigListEntry(_('Wiki TV'), config.plugins.EtPortal.none))
        #if isPluginInstalled('XBMCAddons'):
        #    self.list.append(getConfigListEntry(_('xbmc - addons'), config.plugins.EtPortal.xbmcaddons))
        #else:
        #    self.list.append(getConfigListEntry(_('xbmc - addons'), config.plugins.EtPortal.none))
        if isPluginInstalled('OpenXtaReader'):
            self.list.append(getConfigListEntry(_('OpenXTA Forum Reader'), config.plugins.EtPortal.xtrend))
        else:
            self.list.append(getConfigListEntry(_('OpenXTA Forum Reader'), config.plugins.EtPortal.none))
        if isPluginInstalled('YahooWeather'):
            self.list.append(getConfigListEntry(_('Yahoo Weather'), config.plugins.EtPortal.yahooweather))
        else:
            self.list.append(getConfigListEntry(_('Yahoo Weather'), config.plugins.EtPortal.none))
        if isPluginInstalled('YampMusicPlayer'):
            self.list.append(getConfigListEntry(_('Yamp Music Player'), config.plugins.EtPortal.yamp))
        else:
            self.list.append(getConfigListEntry(_('Yamp Music Player'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_(' '), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('mod by: mogli123 / icewaere / pcd / koivo'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('thx to bla666'), config.plugins.EtPortal.none))
        self['config'].list = self.list
        self['config'].l.setList(self.list)

    def keyLeft(self):
        ConfigListScreen.keyLeft(self)

    def keyRight(self):
        ConfigListScreen.keyRight(self)

    def keyGet(self):
        if config.plugins.EtPortal.Get.value:
            config.plugins.EtPortal.Get.setValue(False)
            self.session.open(MessageBox, _('Info Button: off'), MessageBox.TYPE_INFO, timeout=4)
        else:
            config.plugins.EtPortal.Get.setValue(True)
            self.session.open(MessageBox, _('Info Button: on'), MessageBox.TYPE_INFO, timeout=4)
        config.plugins.EtPortal.Get.save()

    def up(self):
        self['config'].instance.moveSelection(self['config'].instance.pageUp)

    def down(self):
        self['config'].instance.moveSelection(self['config'].instance.pageDown)

    def keyGo(self):
        for x in self['config'].list:
            x[1].save()

        self.close()

    def keyCancel(self):
        for x in self['config'].list:
            x[1].cancel()

        self.close()


def SkinWidthHD():
    if skin_w  >= 1280:
        return True
    else:
        return False
        
        
def main(session, **kwargs):
    session.open(EtPortalSetupScreen)


def main2(session, **kwargs):
    if SkinWidthHD():
        session.open(EtPortalScreen)
    else:
        session.open(MessageBox, _('EtPortal\n\nSorry.. No Support for Skin Resolution Size: \n\nSD:  720x576 px\nXD: 1024x720 px\n\n________________________________________\n\nSupported: \n\nHD: 1280x720 px\nFullHD: 1920x1080 px'), type=MessageBox.TYPE_INFO, timeout=25)


def main3(session, **kwargs):
    if SkinWidthHD():
        session.open(EtPortalScreen)
    else:
        session.open(MessageBox, _('EtPortal\n\nSorry.. No Support for Skin Resolution Size: \n\nSD:  720x576 px\nXD: 1024x720 px\n\n________________________________________\n\nSupported: \n\nHD: 1280x720 px\nFullHD: 1920x1080 px'), type=MessageBox.TYPE_INFO, timeout=25)


def markButtonHook(self):
    if SkinWidthHD():
        self.session.open(EtPortalScreen)
    else:
        self.session.open(MessageBox, _('EtPortal\n\nSorry.. No Support for Skin Resolution Size: \n\nSD:  720x576 px\nXD: 1024x720 px\n\n________________________________________\n\nSupported: \n\nHD: 1280x720 px\nFullHD: 1920x1080 px'), type=MessageBox.TYPE_INFO, timeout=25)


def timerButtonHook(self):
    from Screens.TimerEdit import TimerEditList
    self.session.open(TimerEditList)


def InfoBarPlugins__init__(self):
    global baseInfoBarPlugins__init__
    if config.plugins.EtPortal.enablemarkbutton.value:
        config.plugins.EtPortal.enablemarkbutton.setValue(True)
        self['EtPortalActions'] = ActionMap(['EtPortalActions'], 
        {'mark_button': self.buttonHookMark,
         'timer_button': self.buttonHookTimer}, -1)
    baseInfoBarPlugins__init__(self)


def autostart(reason, **kwargs):
    global baseInfoBarPlugins__init__
    if 'session' in kwargs:
        baseInfoBarPlugins__init__ = InfoBarPlugins.__init__
        InfoBarPlugins.__init__ = InfoBarPlugins__init__
        if config.plugins.EtPortal.enablemarkbutton.value:
            InfoBarPlugins.buttonHookMark = markButtonHook
            InfoBarPlugins.buttonHookTimer = timerButtonHook


def Plugins(**kwargs):
    return [PluginDescriptor(where=PluginDescriptor.WHERE_SESSIONSTART, fnc=autostart),
     PluginDescriptor(name=_('EtPortal Setup')+" "+EtPortalVersion, description=_('EtPortal Setup'), where=PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main),
     PluginDescriptor(name=_('EtPortal'), description=_('Inofficial')+" "+EtPortalVersion, where=PluginDescriptor.WHERE_PLUGINMENU, icon='plugin.png', fnc=main2),
     PluginDescriptor(name=_('EtPortal Inofficial')+" "+EtPortalVersion, description=_('EtPortal'), where=PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main3)]
