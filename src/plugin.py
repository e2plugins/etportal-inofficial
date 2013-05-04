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
from enigma import ePicLoad, eTimer
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.InfoBarGenerics import InfoBarPlugins
from Tools.Directories import pathExists, resolveFilename
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from Components.AVSwitch import AVSwitch
from Tools.Directories import fileExists, pathExists
from Components.ConfigList import ConfigListScreen
from Components.config import config, ConfigSubsection, ConfigBoolean, getConfigListEntry, ConfigYesNo, ConfigText, ConfigSelection, ConfigPassword, NoSave, ConfigNothing
import keymapparser
import os
import os.path
from Screens.PluginBrowser import PluginBrowser
from Components.PluginList import *
from Components.Pixmap import MovingPixmap
from __init__ import _

EtPortal_version = '3.1'
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

config.plugins.EtPortal = ConfigSubsection()
config.plugins.EtPortal.finalexit = ConfigBoolean(default=False)
config.plugins.EtPortal.rememberposition = ConfigYesNo(default=True)
config.plugins.EtPortal.showtimericon = ConfigBoolean(default=True)
config.plugins.EtPortal.enablemarkbutton = ConfigYesNo(default=True)
config.plugins.EtPortal.vfd = ConfigYesNo(default=True)
config.plugins.EtPortal.adult = ConfigPassword(default='', visible_width=50, fixed_size=False)
config.plugins.EtPortal.Get = ConfigYesNo(default=False)
config.plugins.EtPortal.movie = ConfigYesNo(default=True)
config.plugins.EtPortal.emc = ConfigYesNo(default=False)
config.plugins.EtPortal.dvd = ConfigYesNo(default=False)
config.plugins.EtPortal.laola = ConfigYesNo(default=False)
config.plugins.EtPortal.songs = ConfigYesNo(default=False)
config.plugins.EtPortal.media = ConfigYesNo(default=False)
config.plugins.EtPortal.picture = ConfigYesNo(default=True)
config.plugins.EtPortal.mytube = ConfigYesNo(default=False)
config.plugins.EtPortal.etstreams = ConfigYesNo(default=False)
config.plugins.EtPortal.cinestream = ConfigYesNo(default=False)
config.plugins.EtPortal.burning = ConfigYesNo(default=False)
config.plugins.EtPortal.kinokiste = ConfigYesNo(default=False)
config.plugins.EtPortal.webmedia = ConfigYesNo(default=False)
config.plugins.EtPortal.moviestream = ConfigYesNo(default=False)
config.plugins.EtPortal.musicstream = ConfigYesNo(default=False)
config.plugins.EtPortal.loads7 = ConfigYesNo(default=False)
config.plugins.EtPortal.webbrowser = ConfigYesNo(default=False)
config.plugins.EtPortal.weather = ConfigYesNo(default=False)
config.plugins.EtPortal.wetter = ConfigYesNo(default=False)
config.plugins.EtPortal.weblinks = ConfigYesNo(default=False)
config.plugins.EtPortal.merlinmusic = ConfigYesNo(default=False)
config.plugins.EtPortal.foreca = ConfigYesNo(default=False)
config.plugins.EtPortal.onechannel = ConfigYesNo(default=False)
config.plugins.EtPortal.m2k = ConfigYesNo(default=False)
config.plugins.EtPortal.m2ks = ConfigYesNo(default=False)
config.plugins.EtPortal.putpat = ConfigYesNo(default=False)
config.plugins.EtPortal.istream = ConfigYesNo(default=False)
config.plugins.EtPortal.myvideo = ConfigYesNo(default=False)
config.plugins.EtPortal.tvspielfilm = ConfigYesNo(default=False)
config.plugins.EtPortal.extensions = ConfigYesNo(default=True)
config.plugins.EtPortal.pluginbrowser = ConfigYesNo(default=True)
config.plugins.EtPortal.shutdown = ConfigYesNo(default=True)
config.plugins.EtPortal.systeminfo = ConfigYesNo(default=True)
config.plugins.EtPortal.myentertainment = ConfigYesNo(default=False)
config.plugins.EtPortal.netzkino = ConfigYesNo(default=False)
config.plugins.EtPortal.tvkino = ConfigYesNo(default=False)
config.plugins.EtPortal.hoerspiel = ConfigYesNo(default=False)
config.plugins.EtPortal.livetvru = ConfigYesNo(default=False)
config.plugins.EtPortal.dreamexplorer = ConfigYesNo(default=True)
config.plugins.EtPortal.digitalfernsehen = ConfigYesNo(default=True)
config.plugins.EtPortal.Chefkoch = ConfigYesNo(default=True)
config.plugins.EtPortal.bluray = ConfigYesNo(default=True)
config.plugins.EtPortal.bild = ConfigYesNo(default=True)
config.plugins.EtPortal.kinode = ConfigYesNo(default=True)
config.plugins.EtPortal.spiegel = ConfigYesNo(default=True)
config.plugins.EtPortal.focus = ConfigYesNo(default=True)
config.plugins.EtPortal.wiki = ConfigYesNo(default=True)
config.plugins.EtPortal.kinderkino = ConfigYesNo(default=True)
config.plugins.EtPortal.doku = ConfigYesNo(default=True)
config.plugins.EtPortal.myspass = ConfigYesNo(default=True)
config.plugins.EtPortal.kicker = ConfigYesNo(default=False)
config.plugins.EtPortal.kickerticker = ConfigYesNo(default=False)
config.plugins.EtPortal.verkehrsinfo = ConfigYesNo(default=True)
config.plugins.EtPortal.cubicstreamer = ConfigYesNo(default=False)
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
config.plugins.EtPortal.myvideoplus = ConfigYesNo(default=True)
config.plugins.EtPortal.youtubeplus = ConfigYesNo(default=True)
config.plugins.EtPortal.ondemand = ConfigYesNo(default=True)
config.plugins.EtPortal.mp3browser = ConfigYesNo(default=True)
config.plugins.EtPortal.moviebrowser = ConfigYesNo(default=True)
config.plugins.EtPortal.pvmc = ConfigYesNo(default=True)
config.plugins.EtPortal.webradiofs = ConfigYesNo(default=True)

config.plugins.EtPortal.none = NoSave(ConfigNothing()) 
config.plugins.EtPortal.color = ConfigSelection(default='SkinColor', choices=[('iceHD', _('iceHD')), ('black', _('black')), ('Nobile', _('Nobile')), ('SkinColor', _('SkinColor'))])

def writeToVFD(txt):
    if config.plugins.EtPortal.vfd.value:
        oled = '/dev/dbox/oled0'
        if fileExists(oled):
            tmp = open(oled, 'w')
            tmp.write(txt[:124])
            tmp.close()


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
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/DreamExplorer/plugin.pyo') and config.plugins.EtPortal.dreamexplorer.value:
            piclist.append(('dreamexplorer.png', _('DreamExplorer')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/DVDPlayer/keymap.xml') and config.plugins.EtPortal.dvd.value:
            piclist.append(('dvd_player.png', _('DVD Player')))
        if fileExists('/usr/lib/enigma2/python/Screens/DVD.pyo') and config.plugins.EtPortal.dvd.value:
            piclist.append(('dvd_player.png', _('DVD Player')))
        if config.plugins.EtPortal.media.value:
            piclist.append(('media_player.png', _('Media Player')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/EnhancedMovieCenter/plugin.pyo') and config.plugins.EtPortal.emc.value:
            piclist.append(('emc.png', _('Enhanced Movie-Center')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/PicturePlayer/ui.pyo') and config.plugins.EtPortal.picture.value:
            piclist.append(('picture_player.png', _('Picture Player')))
        if fileExists('/usr/lib/enigma2/python/Plugins/SystemPlugins/NetworkBrowser/NetworkBrowser.pyo') and config.plugins.EtPortal.networkbrowser.value:
            piclist.append(('network.png', _('Network Browser')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MyTube/plugin.pyo') and config.plugins.EtPortal.mytube.value:
            piclist.append(('mytube.png', _('My TubePlayer')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/EtStreams/plugin.pyo') and config.plugins.EtPortal.etstreams.value:
            piclist.append(('etstreams.png', _('ET-Streams')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/cinestreamer/plugin.pyo') and config.plugins.EtPortal.cinestream.value:
            piclist.append(('cinestream.png', _('CineStream')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/laola1tvlive/plugin.pyo') and config.plugins.EtPortal.laola.value:
            piclist.append(('laolatv.png', _('laola1.tv')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/songs/plugin.pyo') and config.plugins.EtPortal.songs.value:
            piclist.append(('songs.png', _('Songs.to')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kinokiste/plugin.pyo') and config.plugins.EtPortal.kinokiste.value:
            piclist.append(('kinokiste.png', _('KinoKiste')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebMedia/') and config.plugins.EtPortal.webmedia.value:
            piclist.append(('webmedia.png', _('WebMedia')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/burnseries/plugin.pyo') and config.plugins.EtPortal.burning.value:
            piclist.append(('burnseries.png', _('Burning-Series')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/moviestream/plugin.pyo') and config.plugins.EtPortal.moviestream.value:
            piclist.append(('moviestream.png', _('MovieStream')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/musicstream/plugin.pyo') and config.plugins.EtPortal.musicstream.value:
            piclist.append(('musicstream.png', _('MusicStream')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/loads7/plugin.pyo') and config.plugins.EtPortal.loads7.value:
            piclist.append(('loads7.png', _('Loads7')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/movie2kfilme/plugin.pyo') and config.plugins.EtPortal.m2k.value:
            piclist.append(('m2k.png', _('Movie2k - Movies')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/movie2kserien/plugin.pyo') and config.plugins.EtPortal.m2ks.value:
            piclist.append(('m2ks.png', _('Movie2k - Series')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/putpattv/plugin.pyo') and config.plugins.EtPortal.putpat.value:
            piclist.append(('putpat.png', _('putpat.tv')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/istream/plugin.pyo') and config.plugins.EtPortal.istream.value:
            piclist.append(('istream.png', _('iStream')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/chartsplayer/plugin.pyo') and config.plugins.EtPortal.myvideo.value:
            piclist.append(('myvideo.png', _('MyVideo - Top 100')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TVSpielfilm/plugin.pyo') and config.plugins.EtPortal.tvspielfilm.value:
            piclist.append(('tvspielfilm.png', _('TV Spielfilm')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/plugin.pyo') and config.plugins.EtPortal.webbrowser.value:
            piclist.append(('opera.png', _('Web browser')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/msnWetter/plugin.pyo') and config.plugins.EtPortal.weather.value:
            piclist.append(('wetter.png', _('msn-Wetter')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WeatherPlugin/plugin.pyo') and config.plugins.EtPortal.wetter.value:
            piclist.append(('weather.png', _('Wetter')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/weblinks.pyo') and config.plugins.EtPortal.weblinks.value:
            piclist.append(('weblinks.png', _('Weblinks plugin')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/pornkiste/plugin.pyo') and config.plugins.EtPortal.adult.value:
            piclist.append(('pornkiste.png', _('PornKiste 18+')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/YouPorn/plugin.pyo') and config.plugins.EtPortal.adult.value:
            piclist.append(('youporn.png', _('youporn 18+')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/ePorner/plugin.pyo') and config.plugins.EtPortal.adult.value:
            piclist.append(('eporner.png', _('ePorner 18+')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/beeg/plugin.pyo') and config.plugins.EtPortal.adult.value:
            piclist.append(('beeg.png', _('beeg 18+')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/myspass/plugin.pyo') and config.plugins.EtPortal.myspass.value:
            piclist.append(('myspass.png', _('MySpass.de')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MerlinMusicPlayer/plugin.pyo') and config.plugins.EtPortal.merlinmusic.value:
            piclist.append(('merlinmusic.png', _('Merlin Music Player')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/DIGITALfernsehen/plugin.pyo') and config.plugins.EtPortal.digitalfernsehen.value:
            piclist.append(('digitalfernsehen.png', _('DiGITAL fernsehen')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Foreca/plugin.pyo') and config.plugins.EtPortal.foreca.value:
            piclist.append(('foreca.png', _('Foreca Weather')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/1channel/plugin.pyo') and config.plugins.EtPortal.onechannel.value:
            piclist.append(('1channel.png', _('1channel')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/myentertainment/plugin.pyo') and config.plugins.EtPortal.myentertainment.value:
            piclist.append(('my-entertainment.png', _('My-Entertainment.biz')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/netzkino/plugin.pyo') and config.plugins.EtPortal.netzkino.value:
            piclist.append(('netzkino.png', _('NetzKino.de')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/tvkino/plugin.pyo') and config.plugins.EtPortal.tvkino.value:
            piclist.append(('tv-kino.png', _('TV-Kino.net')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/hoerspiele/plugin.pyo') and config.plugins.EtPortal.hoerspiel.value:
            piclist.append(('hoerspiel.png', _('Hoerspiele.cu.cc')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/livetvru/plugin.pyo') and config.plugins.EtPortal.livetvru.value:
            piclist.append(('livetvru.png', _('Live TV')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Chefkoch/plugin.pyo') and config.plugins.EtPortal.Chefkoch.value:
            piclist.append(('chefkoch.png', _('Chefkoch')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Blu-ray/plugin.pyo') and config.plugins.EtPortal.bluray.value:
            piclist.append(('bluray.png', _('BLURAY-DISC')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/BILDOnline/plugin.pyo') and config.plugins.EtPortal.bild.value:
            piclist.append(('bild.png', _('Bild.de')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/KINOde/plugin.pyo') and config.plugins.EtPortal.kinode.value:
            piclist.append(('kino.png', _('Kino.de')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/SPIEGELOnline/plugin.pyo') and config.plugins.EtPortal.spiegel.value:
            piclist.append(('spiegel.png', _('Spiegel ONLINE')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/FOCUSOnline/plugin.pyo') and config.plugins.EtPortal.focus.value:
            piclist.append(('focus.png', _('Focus ONLINE')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Wikipedia/plugin.pyo') and config.plugins.EtPortal.wiki.value:
            piclist.append(('wiki.png', _('Wikipedia')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MUZUtv/plugin.pyo') and config.plugins.EtPortal.muzutv.value:
            piclist.append(('muzutv.png', _('MUZU.TV')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kinderkino/plugin.pyo') and config.plugins.EtPortal.kinderkino.value:
            piclist.append(('kinderkino.png', _('kinderkino')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/dokumonster/plugin.pyo') and config.plugins.EtPortal.doku.value:
            piclist.append(('doku.png', _('dokumonster')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kicker/plugin.pyo') and config.plugins.EtPortal.kicker.value:
            piclist.append(('kicker.png', _('Kicker Online')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kicker/plugin.pyo') and config.plugins.EtPortal.kickerticker.value:
            piclist.append(('kickerticker.png', _('Kicker Live-Ticker')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/verkehrsinfo/plugin.pyo') and config.plugins.EtPortal.verkehrsinfo.value:
            piclist.append(('verkehrsinfo.png', _('verkehrsinfo.de')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Facebook/plugin.pyo') and config.plugins.EtPortal.facebook.value:
            piclist.append(('facebook.png', _('facebook')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/CuBiCStreamer/plugin.pyo') and config.plugins.EtPortal.cubicstreamer.value:
            piclist.append(('cubic.png', _('Cubic Streamer')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/plugin.pyo') and config.plugins.EtPortal.turkvod.value:
            piclist.append(('turkvod.png', _('TURKvod IPTV')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/GreekStreamTV/plugin.pyo') and config.plugins.EtPortal.greekstreamtv.value:
            piclist.append(('greekstreamtv.png', _('Greek StreamTV')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/plugin.pyo') and config.plugins.EtPortal.mediaportal.value:
            piclist.append(('mediaportal.png', _('MediaPortal')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Xtrend/plugin.pyo') and config.plugins.EtPortal.xtrend.value:
            piclist.append(('xtrend.png', _('Xtrend Support Reader')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/YampMusicPlayer/plugin.pyo') and config.plugins.EtPortal.yamp.value:
            piclist.append(('yamp.png', _('Yamp Music Player')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/SHOUTcast/plugin.pyo') and config.plugins.EtPortal.shoutcast.value:
            piclist.append(('shoutcast.png', _('SHOUTcast')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/plugin.pyo') and config.plugins.EtPortal.tunein.value:
            piclist.append(('tunein.png', _('tunein Radio')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/plugin.pyo') and config.plugins.EtPortal.ardhbbtv.value:
            piclist.append(('ardhbbtv.png', _('ARD HbbTV-Portal')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/skyrecorder/plugin.pyo') and config.plugins.EtPortal.skyrecorder.value:
            piclist.append(('skyrecorder.png', _('sky recorder')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MyvideoPlus/plugin.pyo') and config.plugins.EtPortal.myvideoplus.value:
            piclist.append(('myvideoplus.png', _('MyVideo-Plus')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/YoutubePlus/plugin.pyo') and config.plugins.EtPortal.youtubeplus.value:
            piclist.append(('youtubeplus.png', _('YouTube-Plus')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/OnDemand/plugin.pyo') and config.plugins.EtPortal.ondemand.value:
            piclist.append(('ondemand.png', _('On Demand')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MP3Browser/plugin.pyo') and config.plugins.EtPortal.mp3browser.value:
            piclist.append(('mp3browser.png', _('mp3-Browser')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MovieBrowser/plugin.pyo') and config.plugins.EtPortal.moviebrowser.value:
            piclist.append(('moviebrowser.png', _('Movie-Browser')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/ProjectValerie/plugin.pyo') and config.plugins.EtPortal.pvmc.value:
            piclist.append(('valerie.png', _('Project-Valerie')))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/webradioFS/plugin.pyo') and config.plugins.EtPortal.webradiofs.value:
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

        if config.plugins.EtPortal.color.value == 'iceHD':
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
        
        elif config.plugins.EtPortal.color.value == 'black':
            self.skin = '<screen position="0,e-200" size="e-0,200" flags="wfNoBorder" backgroundColor="transparent" >'
            posX = 0
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/pics/sel.png" position="562,0" size="150,130" zPosition="2" transparent="1" alphatest="blend" />'
            self.skin += '<eLabel position="0,75" zPosition="0" size="e-0,e-90" backgroundColor="' + self.color + '" />' + skincontent
            self.skin += '<widget source="label" render="Label" position="0,148" size="e-0,40" halign="center" font="Regular;30" zPosition="2" backgroundColor="#00000000" transparent="1" noWrap="1" foregroundColor="' + self.textcolor + '" />'
            self.skin += '</screen>'
        
        elif config.plugins.EtPortal.color.value == 'SkinColor':
            self.skin = '<screen position="0,e-200" size="e-0,200" flags="wfNoBorder" backgroundColor="transparent" >'
            posX = 0
            self.skin += '<ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/pics/sel.png" position="562,0" size="150,130" zPosition="2" transparent="1" alphatest="blend" />'
            self.skin += '<eLabel position="0,75" zPosition="0" size="e-0,e-90" />' + skincontent
            self.skin += '<widget source="label" render="Label" position="0,148" size="e-0,40" halign="center" font="Regular;30" zPosition="2" backgroundColor="#00000000" transparent="1" noWrap="1" foregroundColor="' + self.textcolor + '" />'
            self.skin += '</screen>'
		
		elif config.plugins.EtPortal.color.value == 'Nobile':
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

        self.maxentry = len(self.filelist) - 1
        if config.plugins.EtPortal.rememberposition.value:
            self.index = global_index
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
        self.newPage()

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
                self.Thumbnaillist.append([0,
                 idx,
                 self.filelist[offset][1],
                 self.filelist[offset][2]])
                offset += 1
            else:
                self.Thumbnaillist.append([0,
                 idx,
                 self.filelist[offset + self.index][1],
                 self.filelist[offset + self.index][2]])
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
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/DreamExplorer/plugin.pyo'):
                from Plugins.Extensions.DreamExplorer.plugin import *
                self.session.open(DreamExplorerII)
        elif 'movie_player.png' in self.Thumbnaillist[3][2]:
            from Screens.InfoBar import InfoBar
            if InfoBar and InfoBar.instance:
                InfoBar.showMovies(InfoBar.instance)
        elif 'media_player.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MediaPlayer/plugin.pyo'):
                from Plugins.Extensions.MediaPlayer.plugin import MediaPlayer
                self.session.open(MediaPlayer)
        elif 'wetter.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/msnWetter/plugin.pyo'):
                from Plugins.Extensions.msnWetter.plugin import *
                self.session.open(colorCheck)
        elif 'weather.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WeatherPlugin/plugin.pyo'):
                from Plugins.Extensions.WeatherPlugin.plugin import MSNWeatherPlugin
                self.session.open(MSNWeatherPlugin)
        elif 'dvd_player.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/DVDPlayer/keymap.xml'):
                from Plugins.Extensions.DVDPlayer.plugin import DVDPlayer
                self.session.open(DVDPlayer)
            if not fileExists('/usr/lib/enigma2/python/Plugins/Extensions/DVDPlayer/keymap.xml') and fileExists('/usr/lib/enigma2/python/Screens/DVD.pyo'):
                from Screens import DVD
                self.session.open(DVD.DVDPlayer)
        elif 'webmedia.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebMedia/'):
                from Plugins.Extensions.WebMedia.plugin import *
                from Components.PluginComponent import plugins
                plugin = _('WebMedia')
                for p in plugins.getPlugins(where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU]):
                    if 'WebMedia' == str(p.name):
                        plugin = p
                if plugin is not None:
                    plugin(session=self.session)
        elif 'emc.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.emc.value:
                from Plugins.Extensions.EnhancedMovieCenter.plugin import *
                from Components.PluginComponent import plugins
                showMoviesNew()
        elif 'picture_player.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/PicturePlayer/ui.pyo'):
                from Plugins.Extensions.PicturePlayer.ui import picshow
                self.session.open(picshow)
        elif 'network.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/SystemPlugins/NetworkBrowser/NetworkBrowser.pyo'):
                from Plugins.SystemPlugins.NetworkBrowser.plugin import *
                iface = None
                self.session.open(NetworkBrowser, iface, plugin_path)
        elif 'mytube.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MyTube/plugin.pyo'):
                from Plugins.Extensions.MyTube.plugin import *
                l2key = True
                self.session.open(MyTubePlayerMainScreen, l2key)
        elif 'etstreams.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/EtStreams/plugin.pyo'):
                from Plugins.Extensions.EtStreams.plugin import *
                self.session.open(EtStreams)
        elif 'cinestream.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/cinestreamer/plugin.pyo'):
                from Plugins.Extensions.cinestreamer.plugin import *
                self.session.open(csmain, plugin_path)
        elif 'laolatv.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/laola1tvlive/plugin.pyo'):
                from Plugins.Extensions.laola1tvlive.plugin import *
                self.session.open(laola, plugin_path)
        elif 'songs.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/songs/plugin.pyo'):
                from Plugins.Extensions.songs.plugin import *
                self.session.open(songsto, plugin_path)
        elif 'm2k.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/movie2kfilme/plugin.pyo'):
                from Plugins.Extensions.movie2kfilme.plugin import *
                self.session.open(movie2k, plugin_path)
        elif 'm2ks.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/movie2kserien/plugin.pyo'):
                from Plugins.Extensions.movie2kserien.plugin import *
                self.session.open(m2kserien, plugin_path)
        elif 'putpat.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/putpattv/plugin.pyo'):
                from Plugins.Extensions.putpattv.plugin import *
                self.session.openWithCallback(closen, putpat, False, start_point_now, plugin_path)
        elif 'istream.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/istream/plugin.pyo'):
                from Plugins.Extensions.istream.plugin import *
                self.session.openWithCallback(closen, istream, plugin_path)
        elif 'doku.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/dokumonster/plugin.pyo'):
                from Plugins.Extensions.dokumonster.plugin import *
                self.session.open(dokumonster, plugin_path)
        elif 'myspass.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/myspass/plugin.pyo'):
                from Plugins.Extensions.myspass.plugin import *
                self.session.open(myspass, plugin_path)
        elif 'kinderkino.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kinderkino/plugin.pyo'):
                from Plugins.Extensions.kinderkino.plugin import *
                self.session.openWithCallback(closen, kinderkino, plugin_path)
        elif 'myvideo.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/chartsplayer/plugin.pyo'):
                from Plugins.Extensions.chartsplayer.plugin import *
                self.session.open(chartsplayer, plugin_path)
        elif 'kinokiste.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kinokiste/plugin.pyo'):
                from Plugins.Extensions.kinokiste.plugin import *
                self.session.open(kinokiste, plugin_path)
        elif 'burnseries.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/burnseries/plugin.pyo'):
                from Plugins.Extensions.burnseries.plugin import *
                self.session.open(burns, plugin_path)
        elif 'tvspielfilm.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TVSpielfilm/plugin.pyo'):
                from Plugins.Extensions.TVSpielfilm.plugin import *
                from Plugins.Extensions.TVSpielfilm.plugin import tvMain
                self.session.open(tvMain)
        elif 'chefkoch.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Chefkoch/plugin.pyo'):
                from Plugins.Extensions.Chefkoch.plugin import *
                self.session.open(ChefkochMain)
        elif 'xtrend.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Xtrend/plugin.pyo'):
                from Plugins.Extensions.Xtrend.plugin import *
                self.session.open(XtrendMain)
        elif 'moviestream.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/moviestream/plugin.pyo'):
                from Plugins.Extensions.moviestream.plugin import *
                self.session.open(moviestream, plugin_path)
        elif 'musicstream.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/musicstream/plugin.pyo'):
                from Plugins.Extensions.musicstream.plugin import *
                self.session.open(ms, plugin_path)
        elif 'loads7.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/loads7/plugin.pyo'):
                from Plugins.Extensions.loads7.plugin import *
                self.session.open(sieben_loads, plugin_path)
        elif 'merlinmusic.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.merlinmusic.value:
                from Plugins.Extensions.MerlinMusicPlayer.plugin import *
                servicelist = None
                self.session.open(MerlinMusicPlayerFileList, servicelist)
        elif 'foreca.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.foreca.value:
                from Plugins.Extensions.Foreca.plugin import *
                self.session.open(ForecaPreview)
        elif '1channel.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.onechannel.value:
                _temp = __import__('Plugins.Extensions.1channel.plugin', globals(), locals(), ['MyMenux'], -1)
                action = 'start'
                value = 0
                MyMenux = _temp.MyMenux
                self.session.open(MyMenux, action, value)
        elif 'pornkiste.png' in self.Thumbnaillist[3][2]:
            password = '/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/adultpassword'
            if fileExists(password):
                c = open(password, 'r')
                for line in c:
                    self.passw = line
                c.close()
            if config.plugins.EtPortal.adult.value == self.passw:
                from Plugins.Extensions.pornkiste.plugin import *
                self.session.open(pornkiste, plugin_path)
            else:
                self.session.open(MessageBox, _('Falsches Passwort!\n\nwrong password!'), MessageBox.TYPE_INFO, timeout=8)
        elif 'eporner.png' in self.Thumbnaillist[3][2]:
            password = '/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/adultpassword'
            if fileExists(password):
                c = open(password, 'r')
                for line in c:
                    self.passw = line
                c.close()
            if config.plugins.EtPortal.adult.value == self.passw:
                from Plugins.Extensions.ePorner.plugin import *
                self.session.open(eporner, plugin_path)
            else:
                self.session.open(MessageBox, _('Falsches Passwort!\n\nwrong password!'), MessageBox.TYPE_INFO, timeout=8)
        elif 'beeg.png' in self.Thumbnaillist[3][2]:
            password = '/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/adultpassword'
            if fileExists(password):
                c = open(password, 'r')
                for line in c:
                    self.passw = line
                c.close()
            if config.plugins.EtPortal.adult.value == self.passw:
                from Plugins.Extensions.beeg.plugin import *
                self.session.openWithCallback(closen, beeg, plugin_path)
            else:
                self.session.open(MessageBox, _('wrong password!'), MessageBox.TYPE_INFO, timeout=8)
        elif 'youporn.png' in self.Thumbnaillist[3][2]:
            password = '/usr/lib/enigma2/python/Plugins/Extensions/EtPortal/adultpassword'
            if fileExists(password):
                c = open(password, 'r')
                for line in c:
                    self.passw = line
                c.close()
            if config.plugins.EtPortal.adult.value == self.passw:
                from Plugins.Extensions.YouPorn.plugin import *
                self.session.open(youpornMain, True)
            else:
                self.session.open(MessageBox, _('wrong password!'), MessageBox.TYPE_INFO, timeout=8)
        elif 'my-entertainment.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.myentertainment.value:
                from Plugins.Extensions.myentertainment.plugin import *
                self.session.openWithCallback(closen, enter, plugin_path)
        elif 'tv-kino.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.tvkino.value:
                from Plugins.Extensions.tvkino.plugin import *
                self.session.openWithCallback(closen, tvkino, plugin_path)
        elif 'netzkino.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.netzkino.value:
                from Plugins.Extensions.netzkino.plugin import *
                self.session.open(netzkino, plugin_path)
        elif 'hoerspiel.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.hoerspiel.value:
                from Plugins.Extensions.hoerspiele.plugin import *
                self.session.openWithCallback(closen, hoerspiel, plugin_path)
        elif 'digitalfernsehen.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.digitalfernsehen.value:
                from Plugins.Extensions.DIGITALfernsehen.plugin import *
                self.session.open(digitalTVMain)
        elif 'bluray.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.bluray.value:
                _temp = __import__('Plugins.Extensions.Blu-ray.plugin', globals(), locals(), ['blurayMain'], -1)
                blurayMain = _temp.blurayMain
                self.session.open(blurayMain)
        elif 'bild.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.bild.value:
                from Plugins.Extensions.BILDOnline.plugin import *
                self.session.open(bildMain)
        elif 'kino.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.kinode.value:
                from Plugins.Extensions.KINOde.plugin import *
                self.session.open(kinoMain)
        elif 'spiegel.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.spiegel.value:
                from Plugins.Extensions.SPIEGELOnline.plugin import *
                self.session.open(spiegelMain)
        elif 'focus.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.focus.value:
                from Plugins.Extensions.FOCUSOnline.plugin import *
                self.session.open(focusMain)
        elif 'wiki.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.wiki.value:
                from Plugins.Extensions.Wikipedia.plugin import *
                self.session.open(wikiMain)
        elif 'livetvru.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.livetvru.value:
                from Plugins.Extensions.livetvru.plugin import *
                self.session.openWithCallback(closen, livetvru, plugin_path)
        elif 'kicker.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kicker/plugin.pyo'):
                from Plugins.Extensions.kicker.plugin import *
                from Plugins.Extensions.kicker.plugin import kickerMain
                self.session.open(kickerMain)
        elif 'kickerticker.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kicker/plugin.pyo'):
                from Plugins.Extensions.kicker.plugin import *
                from Plugins.Extensions.kicker.plugin import tickerMain
                self.session.open(tickerMain)
        elif 'verkehrsinfo.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.verkehrsinfo.value:
                from Plugins.Extensions.verkehrsinfo.plugin import *
                self.session.open(verkehrsinfoMain)
        elif 'muzutv.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.muzutv.value:
                from Plugins.Extensions.MUZUtv.plugin import *
                self.session.open(muzuMain)
        elif 'facebook.png' in self.Thumbnaillist[3][2]:
            if config.plugins.EtPortal.facebook.value:
                from Plugins.Extensions.Facebook.plugin import *
                self.session.open(loginCheck)
        elif 'cubic.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/CuBiCStreamer/plugin.pyo'):
                from Plugins.Extensions.CuBiCStreamer.plugin import *
                self.session.open(MainWindow)
        elif 'ondemand.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/OnDemand/plugin.pyo'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'OnDemand' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'mediaportal.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/plugin.pyo'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'MediaPortal' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'skyrecorder.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/skyrecorder/plugin.pyo'):
                from Plugins.Extensions.skyrecorder.plugin import *
                self.session.open(SkyRecorderMainScreen)
        elif 'mp3browser.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MP3Browser/plugin.pyo'):
                from Plugins.Extensions.MP3Browser.plugin import *
                self.session.open(mp3Browser)
        elif 'moviebrowser.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MovieBrowser/plugin.pyo'):
                from Plugins.Extensions.MovieBrowser.plugin import *
                self.session.open(movieBrowserBackdrop, 0, config.plugins.moviebrowser.filter.value, config.plugins.moviebrowser.filter.value)
        elif 'valerie.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/ProjectValerie/plugin.pyo'):
                from Plugins.Extensions.ProjectValerie.plugin import *
                self.session.open(PVMC_MainMenu)
        elif 'webradiofs.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/webradioFS/plugin.pyo'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'webradioFS' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'yamp.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/YampMusicPlayer/plugin.pyo'):
                from Plugins.Extensions.YampMusicPlayer.plugin import *
                reload(Yamp)
                self.session.open(Yamp.YampScreen)
        elif 'shoutcast.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/SHOUTcast/plugin.pyo'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'SHOUTcast' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'tunein.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/plugin.pyo'):
                from Plugins.Extensions.WebBrowser.plugin import BrowserRemoteControl
                didOpen = True
                url = 'http://ce.radiotime.com'
                self.session.open(BrowserRemoteControl, url)
        elif 'ardhbbtv.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/plugin.pyo'):
                from Plugins.Extensions.WebBrowser.plugin import BrowserRemoteControl
                didOpen = True
                url = 'http://web.ard.de/hbbtv-portal/index.php'
                self.session.open(BrowserRemoteControl, url)
        elif 'turkvod.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/plugin.pyo'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'TURKvod' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'greekstreamtv.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/GreekStreamTV/plugin.pyo'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'GreekStreamTV' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'myvideoplus.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MyvideoPlus/plugin.pyo'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'MyvideoPlus' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'youtubeplus.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/YoutubePlus/plugin.pyo'):
                from Screens.PluginBrowser import PluginBrowser
                from Plugins.Plugin import PluginDescriptor
                from Components.PluginList import *
                from Components.PluginComponent import plugins
                pluginlist = []
                pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
                for plugin in pluginlist:
                    if 'YoutubePlus' in str(plugin.name):
                        break
                plugin(session=self.session)
        elif 'opera.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/plugin.pyo'):
                from Plugins.Extensions.WebBrowser.plugin import BrowserRemoteControl
            if config.plugins.WebBrowser.hasstartpage.value:
                self.session.open(BrowserRemoteControl, config.plugins.WebBrowser.startpage.value, config.plugins.WebBrowser.startpagemode.value, config.plugins.WebBrowser.startpageagent.value, False)
            else:
                self.session.open(BrowserRemoteControl, '', False, False, True)
        elif 'weblinks.png' in self.Thumbnaillist[3][2]:
            if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/weblinks.pyo'):
                from Plugins.Extensions.WebBrowser.weblinks import WebLinksSelectMenu
                self.session.open(WebLinksSelectMenu)
        elif 'extensions_plugins.png' in self.Thumbnaillist[3][2]:
            from Screens.InfoBar import InfoBar
            if InfoBar and InfoBar.instance:
                InfoBar.showExtensionSelection(InfoBar.instance)
        elif 'plugins.png' in self.Thumbnaillist[3][2]:
            from Screens.PluginBrowser import PluginBrowser
            self.session.open(PluginBrowser)
        if config.plugins.EtPortal.finalexit.value:
            if 'movie_player.png' in self.Thumbnaillist[3][2]:
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
                    from Plugins.Extensions.Wikipedia.plugin import *
                    self.session.open(wikiEvent)
            elif 'tvspielfilm.png' in self.Thumbnaillist[3][2]:
                if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TVSpielfilm/plugin.pyo'):
                    from Plugins.Extensions.TVSpielfilm.plugin import *
                    from Plugins.Extensions.TVSpielfilm.plugin import tvEvent
                    self.session.open(tvEvent)
            elif 'moviebrowser.png' in self.Thumbnaillist[3][2]:
                if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MovieBrowser/plugin.pyo'):
                    from Plugins.Extensions.MovieBrowser.plugin import *
                    self.session.open(movieBrowserPosterwall, 0, config.plugins.moviebrowser.filter.value, config.plugins.moviebrowser.filter.value)

class EtPortalSetupScreen(Screen, ConfigListScreen):
    skin = """
	<screen position="c-300,c-250" size="600,500" title="EtPortal %s %s">
		<widget name="config" position="25,25" scrollbarMode="showOnDemand" size="550,400" />
		<ePixmap pixmap="skin_default/buttons/red.png" position="20,e-45" size="140,40" alphatest="on" />
		<ePixmap pixmap="skin_default/buttons/green.png" position="160,e-45" size="140,40" alphatest="on" />
		<widget source="key_red" render="Label" position="20,e-45" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />
		<widget source="key_green" render="Label" position="160,e-45" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />
	</screen>""" % (EtPortal_version, _("Setup"))
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
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/pornkiste/plugin.pyo') or fileExists('/usr/lib/enigma2/python/Plugins/Extensions/ePorner/plugin.pyo') or fileExists('/usr/lib/enigma2/python/Plugins/Extensions/beeg/plugin.pyo') or fileExists('/usr/lib/enigma2/python/Plugins/Extensions/YouPorn/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Adult-Content 18+'), config.plugins.EtPortal.adult))
        else:
            self.list.append(getConfigListEntry(_('Adult-Content 18+'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/1channel/plugin.pyo'):
            self.list.append(getConfigListEntry(_('1channel'), config.plugins.EtPortal.onechannel))
        else:
            self.list.append(getConfigListEntry(_('1channel'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/plugin.pyo'):
            self.list.append(getConfigListEntry(_('ARD HbbTV-Portal'), config.plugins.EtPortal.ardhbbtv))
        else:
            self.list.append(getConfigListEntry(_('ARD HbbTV-Portal'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/BILDOnline/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Bild.de'), config.plugins.EtPortal.bild))
        else:
            self.list.append(getConfigListEntry(_('Bild.de'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Blu-ray/plugin.pyo'):
            self.list.append(getConfigListEntry(_('BLURAY-DISC.de'), config.plugins.EtPortal.bluray))
        else:
            self.list.append(getConfigListEntry(_('BLURAY-DISC.de'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/burnseries/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Burning-Series'), config.plugins.EtPortal.burning))
        else:
            self.list.append(getConfigListEntry(_('Burning-Series'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Chefkoch/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Chefkoch.de'), config.plugins.EtPortal.Chefkoch))
        else:
            self.list.append(getConfigListEntry(_('Chefkoch.de'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/cinestreamer/plugin.pyo'):
            self.list.append(getConfigListEntry(_('CineStream'), config.plugins.EtPortal.cinestream))
        else:
            self.list.append(getConfigListEntry(_('CineStream'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/CuBiCStreamer/plugin.pyo'):
            self.list.append(getConfigListEntry(_('CuBiC Streamer'), config.plugins.EtPortal.cubicstreamer))
        else:
            self.list.append(getConfigListEntry(_('CuBiC Streamer'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/DIGITALfernsehen/plugin.pyo'):
            self.list.append(getConfigListEntry(_('DiGITAL fernsehen'), config.plugins.EtPortal.digitalfernsehen))
        else:
            self.list.append(getConfigListEntry(_('DiGITAL fernsehen'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/dokumonster/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Dokumonster'), config.plugins.EtPortal.doku))
        else:
            self.list.append(getConfigListEntry(_('Dokumonster'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/DVDPlayer/keymap.xml'):
            self.list.append(getConfigListEntry(_('DVD-Player'), config.plugins.EtPortal.dvd))
        else:
            self.list.append(getConfigListEntry(_('DVD-Player'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/DreamExplorer/plugin.pyo'):
            self.list.append(getConfigListEntry(_('DreamExplorer'), config.plugins.EtPortal.dreamexplorer))
        else:
            self.list.append(getConfigListEntry(_('DreamExplorer'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/EnhancedMovieCenter/plugin.pyo'):
            self.list.append(getConfigListEntry(_('EMC'), config.plugins.EtPortal.emc))
        else:
            self.list.append(getConfigListEntry(_('EMC'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/EtStreams/plugin.pyo'):
            self.list.append(getConfigListEntry(_('EtStreams'), config.plugins.EtPortal.etstreams))
        else:
            self.list.append(getConfigListEntry(_('EtStreams'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Extension Plugins and applications'), config.plugins.EtPortal.extensions))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Facebook/plugin.pyo'):
            self.list.append(getConfigListEntry(_('facebook'), config.plugins.EtPortal.facebook))
        else:
            self.list.append(getConfigListEntry(_('facebook'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/FOCUSOnline/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Focus ONLINE'), config.plugins.EtPortal.focus))
        else:
            self.list.append(getConfigListEntry(_('Focus ONLINE'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Foreca/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Foreca'), config.plugins.EtPortal.foreca))
        else:
            self.list.append(getConfigListEntry(_('Foreca'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/GreekStreamTV/plugin.pyo'):
            self.list.append(getConfigListEntry(_('GreekStreamTV'), config.plugins.EtPortal.greekstreamtv))
        else:
            self.list.append(getConfigListEntry(_('GreekStreamTV'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/hoerspiele/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Hoerspiele'), config.plugins.EtPortal.hoerspiel))
        else:
            self.list.append(getConfigListEntry(_('Hoerspiele'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/istream/plugin.pyo'):
            self.list.append(getConfigListEntry(_('iStream'), config.plugins.EtPortal.istream))
        else:
            self.list.append(getConfigListEntry(_('iStream'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kicker/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Kicker Online'), config.plugins.EtPortal.kicker))
        else:
            self.list.append(getConfigListEntry(_('Kicker Online'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kicker/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Kicker Live-Ticker'), config.plugins.EtPortal.kickerticker))
        else:
            self.list.append(getConfigListEntry(_('Kicker Live-Ticker'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kinderkino/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Kinderkino'), config.plugins.EtPortal.kinderkino))
        else:
            self.list.append(getConfigListEntry(_('Kinderkino'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/KINOde/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Kino.de'), config.plugins.EtPortal.kinode))
        else:
            self.list.append(getConfigListEntry(_('Kino.de'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/kinokiste/plugin.pyo'):
            self.list.append(getConfigListEntry(_('KinoKiste'), config.plugins.EtPortal.kinokiste))
        else:
            self.list.append(getConfigListEntry(_('KinoKiste'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/laola1tvlive/plugin.pyo'):
            self.list.append(getConfigListEntry(_('laola1.tv'), config.plugins.EtPortal.laola))
        else:
            self.list.append(getConfigListEntry(_('laola1.tv'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/livetvru/plugin.pyo'):
            self.list.append(getConfigListEntry(_('LiveTV.ru'), config.plugins.EtPortal.livetvru))
        else:
            self.list.append(getConfigListEntry(_('LiveTV.ru'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/loads7/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Loads7'), config.plugins.EtPortal.loads7))
        else:
            self.list.append(getConfigListEntry(_('Loads7'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Media-Player'), config.plugins.EtPortal.media))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Media Portal'), config.plugins.EtPortal.mediaportal))
        else:
            self.list.append(getConfigListEntry(_('Media Portal'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MerlinMusicPlayer/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Merlin-Music Player'), config.plugins.EtPortal.merlinmusic))
        else:
            self.list.append(getConfigListEntry(_('Merlin-Music Player'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/movie2kfilme/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Movie2k - Movies'), config.plugins.EtPortal.m2k))
        else:
            self.list.append(getConfigListEntry(_('Movie2k - Movies'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/movie2kserien/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Movie2k - Series'), config.plugins.EtPortal.m2ks))
        else:
            self.list.append(getConfigListEntry(_('Movie2k - Series'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Movielist'), config.plugins.EtPortal.movie))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MovieBrowser/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Movie-Browser'), config.plugins.EtPortal.moviebrowser))
        else:
            self.list.append(getConfigListEntry(_('Movie-Browser'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/moviestream/plugin.pyo'):
            self.list.append(getConfigListEntry(_('MovieStream'), config.plugins.EtPortal.moviestream))
        else:
            self.list.append(getConfigListEntry(_('MovieStream'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MP3Browser/plugin.pyo'):
            self.list.append(getConfigListEntry(_('mp3-Browser'), config.plugins.EtPortal.mp3browser))
        else:
            self.list.append(getConfigListEntry(_('mp3-Browser'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/msnWetter/plugin.pyo'):
            self.list.append(getConfigListEntry(_('MSN-Weather'), config.plugins.EtPortal.weather))
        else:
            self.list.append(getConfigListEntry(_('MSN-Weather'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/musicstream/plugin.pyo'):
            self.list.append(getConfigListEntry(_('MusicStream'), config.plugins.EtPortal.musicstream))
        else:
            self.list.append(getConfigListEntry(_('MusicStream'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MUZUtv/plugin.pyo'):
            self.list.append(getConfigListEntry(_('MUZU.TV'), config.plugins.EtPortal.muzutv))
        else:
            self.list.append(getConfigListEntry(_('MUZU.TV'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/myentertainment/plugin.pyo'):
            self.list.append(getConfigListEntry(_('My-Entertainment.biz'), config.plugins.EtPortal.myentertainment))
        else:
            self.list.append(getConfigListEntry(_('My-Entertainment.biz'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MyTube/plugin.pyo'):
            self.list.append(getConfigListEntry(_('MyTube'), config.plugins.EtPortal.mytube))
        else:
            self.list.append(getConfigListEntry(_('MyTube'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/myspass/plugin.pyo'):
            self.list.append(getConfigListEntry(_('MySpass.de'), config.plugins.EtPortal.myspass))
        else:
            self.list.append(getConfigListEntry(_('MySpass.de'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/chartsplayer/plugin.pyo'):
            self.list.append(getConfigListEntry(_('MyVideo - Top 100'), config.plugins.EtPortal.myvideo))
        else:
            self.list.append(getConfigListEntry(_('MyVideo - Top 100'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/MyvideoPlus/plugin.pyo'):
            self.list.append(getConfigListEntry(_('MyVideo-Plus'), config.plugins.EtPortal.myvideoplus))
        else:
            self.list.append(getConfigListEntry(_('MyVideo-Plus'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/SystemPlugins/NetworkBrowser/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Network Browser'), config.plugins.EtPortal.networkbrowser))
        else:
            self.list.append(getConfigListEntry(_('Network Browser'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/netzkino/plugin.pyo'):
            self.list.append(getConfigListEntry(_('NetzKino.de'), config.plugins.EtPortal.netzkino))
        else:
            self.list.append(getConfigListEntry(_('NetzKino.de'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/OnDemand/plugin.pyo'):
            self.list.append(getConfigListEntry(_('On Demand'), config.plugins.EtPortal.ondemand))
        else:
            self.list.append(getConfigListEntry(_('On Demand'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/PicturePlayer/ui.pyo'):
            self.list.append(getConfigListEntry(_('Picture Player'), config.plugins.EtPortal.picture))
        else:
            self.list.append(getConfigListEntry(_('Picture Player'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Plugin Browser'), config.plugins.EtPortal.pluginbrowser))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/putpattv/plugin.pyo'):
            self.list.append(getConfigListEntry(_('putpat.tv'), config.plugins.EtPortal.putpat))
        else:
            self.list.append(getConfigListEntry(_('putpat.tv'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('Sleeptimer and power control'), config.plugins.EtPortal.shutdown))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/SHOUTcast/plugin.pyo'):
            self.list.append(getConfigListEntry(_('SHOUTcast'), config.plugins.EtPortal.shoutcast))
        else:
            self.list.append(getConfigListEntry(_('SHOUTcast'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/skyrecorder/plugin.pyo'):
            self.list.append(getConfigListEntry(_('sky recorder'), config.plugins.EtPortal.skyrecorder))
        else:
            self.list.append(getConfigListEntry(_('sky recorder'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/songs/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Songs.to'), config.plugins.EtPortal.songs))
        else:
            self.list.append(getConfigListEntry(_('Songs.to'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/SPIEGELOnline/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Spiegel ONLINE'), config.plugins.EtPortal.spiegel))
        else:
            self.list.append(getConfigListEntry(_('Spiegel ONLINE'), config.plugins.EtPortal.none))
        self.list.append(getConfigListEntry(_('System Information'), config.plugins.EtPortal.systeminfo))
        self.list.append(getConfigListEntry(_('Timer Option'), config.plugins.EtPortal.showtimericon))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/plugin.pyo'):
            self.list.append(getConfigListEntry(_('tunein Radio'), config.plugins.EtPortal.tunein))
        else:
            self.list.append(getConfigListEntry(_('tunein Radio'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TURKvod/plugin.pyo'):
            self.list.append(getConfigListEntry(_('TURKvod IPTV'), config.plugins.EtPortal.turkvod))
        else:
            self.list.append(getConfigListEntry(_('TURKvod IPTV'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/tvkino/plugin.pyo'):
            self.list.append(getConfigListEntry(_('TV-Kino.net'), config.plugins.EtPortal.tvkino))
        else:
            self.list.append(getConfigListEntry(_('TV-Kino.net'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TVSpielfilm/plugin.pyo'):
            self.list.append(getConfigListEntry(_('TVSpielfilm'), config.plugins.EtPortal.tvspielfilm))
        else:
            self.list.append(getConfigListEntry(_('TVSpielfilm'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/ProjectValerie/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Project-Valerie'), config.plugins.EtPortal.pvmc))
        else:
            self.list.append(getConfigListEntry(_('Project-Valerie'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/verkehrsinfo/plugin.pyo'):
            self.list.append(getConfigListEntry(_('verkehrsinfo.de'), config.plugins.EtPortal.verkehrsinfo))
        else:
            self.list.append(getConfigListEntry(_('verkehrsinfo.de'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WeatherPlugin/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Weather'), config.plugins.EtPortal.wetter))
        else:
            self.list.append(getConfigListEntry(_('Weather'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/plugin.pyo'):
            self.list.append(getConfigListEntry(_('WebBrowser'), config.plugins.EtPortal.webbrowser))
        else:
            self.list.append(getConfigListEntry(_('WebBrowser'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebBrowser/weblinks.pyo'):
            self.list.append(getConfigListEntry(_('WebLinks'), config.plugins.EtPortal.weblinks))
        else:
            self.list.append(getConfigListEntry(_('Weblinks'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/WebMedia/plugin.pyo'):
            self.list.append(getConfigListEntry(_('WebMedia'), config.plugins.EtPortal.webmedia))
        else:
            self.list.append(getConfigListEntry(_('WebMedia'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/webradioFS/plugin.pyo'):
            self.list.append(getConfigListEntry(_('WebRadio FS'), config.plugins.EtPortal.webradiofs))
        else:
            self.list.append(getConfigListEntry(_('WebRadio FS'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Wikipedia/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Wikipedia'), config.plugins.EtPortal.wiki))
        else:
            self.list.append(getConfigListEntry(_('Wikipedia'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/Xtrend/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Xtrend Support Reader'), config.plugins.EtPortal.xtrend))
        else:
            self.list.append(getConfigListEntry(_('Xtrend Support Reader'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/YampMusicPlayer/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Yamp Music Player'), config.plugins.EtPortal.yamp))
        else:
            self.list.append(getConfigListEntry(_('Yamp Music Player'), config.plugins.EtPortal.none))
        if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/YoutubePlus/plugin.pyo'):
            self.list.append(getConfigListEntry(_('Youtube-Plus'), config.plugins.EtPortal.youtubeplus))
        else:
            self.list.append(getConfigListEntry(_('Youtube-Plus'), config.plugins.EtPortal.none))
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


def main(session, **kwargs):
    session.open(EtPortalSetupScreen)


def main2(session, **kwargs):
    session.open(EtPortalScreen)


def main3(session, **kwargs):
    session.open(EtPortalScreen)


def markButtonHook(self):
    self.session.open(EtPortalScreen)


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
     PluginDescriptor(name=_('EtPortal Setup v3.1'), description=_('EtPortal Setup'), where=PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main),
     PluginDescriptor(name=_('EtPortal'), description=_('Inofficial v3.1'), where=PluginDescriptor.WHERE_PLUGINMENU, icon='plugin.png', fnc=main2),
     PluginDescriptor(name=_('EtPortal Inofficial v3.1'), description=_('EtPortal'), where=PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main3)]
