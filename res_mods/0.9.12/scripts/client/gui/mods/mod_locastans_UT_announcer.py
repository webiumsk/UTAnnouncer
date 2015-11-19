# Embedded file name: locastans_UT_announcer
"""for 0.9.12 fixed by webium, all credits goes to locastan"""
import BigWorld
import BattleReplay
#from gui.shared.utils.sound import Sound
from debug_utils import LOG_NOTE, LOG_ERROR
from gui.Scaleform import Battle
from gui.Scaleform.daapi.view.battle.TimersBar import TimersBar
from gui.app_loader import g_appLoader
from string import Template
from Avatar import PlayerAvatar as pa
import ClientArena
import cPickle
from gui.scaleform.daapi.view.battle.meta import DamagePanelMeta
import SoundGroups
import FMOD

class WebiumSound(object):

    def __init__(self, soundPath):
        self.__sndTick = None
        if FMOD.enabled:
            self.__sndTick = SoundGroups.g_instance.playSound2D(soundPath)
        self.__isPlaying = True
        self.stop()
        return

    @property
    def isPlaying(self):
        return self.__isPlaying

    @property
    def fmodSound(self):
        return self.__sndTick

    def play(self):
        if FMOD.enabled:
            self.stop()
            if self.__sndTick:
                self.__sndTick.play()
            self.__isPlaying = True

    def stop(self):
        if self.__sndTick:
            self.__sndTick.stop()
        self.__isPlaying = False
        
pa.firstBlood = None
pa.sndFirstOne = None
pa.sndDouble = None
pa.sndTriple = None
pa.ultraKill = None
pa.multiKill = None
pa.monsterKill = None
pa.killingSpree = None
pa.rampageKill = None
pa.unstopKill = None
pa.godKill = None
pa.elevenKill = None
pa.twelveKill = None
pa.thirteenKill = None
pa.fourteenKill = None
pa.fifteenKill = None
pa.kamikazeSnd = None
pa.ramkillSnd = None
pa.biaSnd = None
pa.crucialSnd = None
pa.deniedSnd = None
pa.paybackSnd = None
pa.snd3min = None
pa.snd2min = None
pa.snd1min = None
pa.snd30sec = None
pa.snd10sec = None
import xml.dom.minidom
import ResMgr
import os

def parsePaths():
    global locaUTConfigFile
    try:
        wd = None
        sec = ResMgr.openSection('../paths.xml')
        subsec = sec['Paths']
        vals = subsec.values()
        for val in vals:
            path = val.asString + '/../'
            if os.path.isdir(path) and os.path.isfile(path + '/configs/UT_announcer.xml'):
                wd = path
                break

        if not wd:
            raise Exception('UT_announcer.xml is not found in the paths')
    except Exception as err:
        print ('[loca_UT] Error locating working directory: ', err)
        wd = 'res_mods/%s/%s' % (ver, os.path.dirname(__file__))
        print '[loca_UT]   fallback to the default path: %s' % wd

    locaUTConfigFile = wd + '/configs/UT_announcer.xml'
    return


parsePaths()
try:
    xmlfile = xml.dom.minidom.parse(locaUTConfigFile)
    logging = xmlfile.getElementsByTagName('logging')[0].childNodes[0].nodeValue
    first = xmlfile.getElementsByTagName('first')[0].childNodes[0].nodeValue
    firstS = xmlfile.getElementsByTagName('one')[0].childNodes[0].nodeValue
    doubleS = xmlfile.getElementsByTagName('two')[0].childNodes[0].nodeValue
    tripleS = xmlfile.getElementsByTagName('three')[0].childNodes[0].nodeValue
    ultraS = xmlfile.getElementsByTagName('four')[0].childNodes[0].nodeValue
    multiS = xmlfile.getElementsByTagName('five')[0].childNodes[0].nodeValue
    monsterS = xmlfile.getElementsByTagName('six')[0].childNodes[0].nodeValue
    spreeS = xmlfile.getElementsByTagName('seven')[0].childNodes[0].nodeValue
    rampS = xmlfile.getElementsByTagName('eight')[0].childNodes[0].nodeValue
    unstopS = xmlfile.getElementsByTagName('nine')[0].childNodes[0].nodeValue
    godS = xmlfile.getElementsByTagName('ten')[0].childNodes[0].nodeValue
    elevenS = xmlfile.getElementsByTagName('eleven')[0].childNodes[0].nodeValue
    twelveS = xmlfile.getElementsByTagName('twelve')[0].childNodes[0].nodeValue
    thirteenS = xmlfile.getElementsByTagName('thirteen')[0].childNodes[0].nodeValue
    fourteenS = xmlfile.getElementsByTagName('fourteen')[0].childNodes[0].nodeValue
    fifteenS = xmlfile.getElementsByTagName('fifteen')[0].childNodes[0].nodeValue
    t10secsS = xmlfile.getElementsByTagName('t10secs')[0].childNodes[0].nodeValue
    t3minsS = xmlfile.getElementsByTagName('t3mins')[0].childNodes[0].nodeValue
    t2minsS = xmlfile.getElementsByTagName('t2mins')[0].childNodes[0].nodeValue
    t1minS = xmlfile.getElementsByTagName('t1min')[0].childNodes[0].nodeValue
    t30secsS = xmlfile.getElementsByTagName('t30secs')[0].childNodes[0].nodeValue
    kamiS = xmlfile.getElementsByTagName('kamikazesound')[0].childNodes[0].nodeValue
    biaS = xmlfile.getElementsByTagName('biasound')[0].childNodes[0].nodeValue
    crucialS = xmlfile.getElementsByTagName('crucialsound')[0].childNodes[0].nodeValue
    ramkillS = xmlfile.getElementsByTagName('ramkillsound')[0].childNodes[0].nodeValue
    paybackS = xmlfile.getElementsByTagName('paybacksound')[0].childNodes[0].nodeValue
    deniedS = xmlfile.getElementsByTagName('deniedsound')[0].childNodes[0].nodeValue
    firsttext = xmlfile.getElementsByTagName('firsttext')[0].childNodes[0].nodeValue
    firstoption = xmlfile.getElementsByTagName('firstoption')[0].childNodes[0].nodeValue
    showtext = xmlfile.getElementsByTagName('showtext')[0].childNodes[0].nodeValue
    kamitext = xmlfile.getElementsByTagName('kamikazetext')[0].childNodes[0].nodeValue
    ramtext = xmlfile.getElementsByTagName('ramkilltext')[0].childNodes[0].nodeValue
    biatext = xmlfile.getElementsByTagName('biatext')[0].childNodes[0].nodeValue
    crucialtext = xmlfile.getElementsByTagName('crucialtext')[0].childNodes[0].nodeValue
    paybacktext = xmlfile.getElementsByTagName('paybacktext')[0].childNodes[0].nodeValue
    paybackowntext = xmlfile.getElementsByTagName('paybackowntext')[0].childNodes[0].nodeValue
    deniedtext = xmlfile.getElementsByTagName('deniedtext')[0].childNodes[0].nodeValue
    delay = int(xmlfile.getElementsByTagName('delay')[0].childNodes[0].nodeValue)
except:
    LOG_ERROR('UT_announcer.xml Problem! File not found or invalid.')
    logging = 'true'
    first = '/webium/killcounter/first'
    firstS = '/webium/killcounter/one'
    doubleS = '/webium/killcounter/two'
    tripleS = '/webium/killcounter/three'
    ultraS = '/webium/killcounter/four'
    multiS = '/webium/killcounter/five'
    monsterS = '/webium/killcounter/six'
    spreeS = '/webium/killcounter/seven'
    rampS = '/webium/killcounter/eight'
    unstopS = '/webium/killcounter/nine'
    godS = '/webium/killcounter/ten'
    elevenS = '/webium/killcounter/eleven'
    twelveS = '/webium/killcounter/twelve'
    thirteenS = '/webium/killcounter/thirteen'
    fourteenS = '/webium/killcounter/fourteen'
    fifteenS = '/webium/killcounter/fifteen'
    t3minsS = '/webium/time/t3mins'
    t2minsS = '/webium/time/t2mins'
    t1minS = '/webium/time/t1min'
    t30secsS = '/webium/time/t30secs'
    t10secsS = '/webium/time/t10secs'
    kamiS = '/locastan/locastan/kamikaze'
    biaS = '/locastan/locastan/eradication'
    crucialS = '/locastan/locastan/extermination'
    ramkillS = '/locastan/locastan/ramkill'
    paybackS = '/locastan/locastan/payback'
    deniedS = '/locastan/locastan/denied'
    firsttext = 'UT_announcer.xml Problem! File not found or invalid.'
    firstoption = 'any'
    showtext = 'true'
    kamitext = 'Kamikaze!'
    ramtext = 'Ramkill!'
    biatext = '$attacker scored us Brothers in Arms!'
    crucialtext = '$attacker scored us Crucial Contribution!'
    paybacktext = '$attacker exerted payback on $target!'
    paybackowntext = '$attacker avenged your death!'
    deniedtext = 'Brothers in Arms denied by $attacker!'
    delay = 2

arenaLength = 0
textCallBackId = None
removeCallBackId = None

def initial():
    BigWorld.player().arena.UT_buddy1 = 0
    BigWorld.player().arena.UT_buddy2 = 0
    BigWorld.player().arena.UT_killer1 = 0
    BigWorld.player().arena.UT_killer2 = 0
    BigWorld.player().arena.UT_ownkiller = 0
    BigWorld.player().arena.BiA = False
    BigWorld.player().arena.Crucial = False
    BigWorld.player().arena.BiAFail = False


def firstone():
    if not pa.sndFirstOne.isPlaying:
        if logging == 'true':
            LOG_NOTE('FirstOne playing')
        pa.sndFirstOne.play()


def double():
    if not pa.sndDouble.isPlaying:
        if logging == 'true':
            LOG_NOTE('Double playing')
        pa.sndDouble.play()


def triple():
    if not pa.sndTriple.isPlaying:
        if logging == 'true':
            LOG_NOTE('Triple playing')
        pa.sndTriple.play()


def ultra():
    if not pa.ultraKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('Ultra playing')
        pa.ultraKill.play()


def multi():
    if not pa.multiKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('Multi playing')
        pa.multiKill.play()


def monster():
    if not pa.monsterKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('Monster playing')
        pa.monsterKill.play()


def spree():
    if not pa.killingSpree.isPlaying:
        if logging == 'true':
            LOG_NOTE('Spree playing')
        pa.killingSpree.play()


def rampage():
    if not pa.rampageKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('Rampage playing')
        pa.rampageKill.play()


def nonstop():
    if not pa.unstopKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('unstoppable playing')
        pa.unstopKill.play()


def godlike():
    if not pa.godKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('Godlike playing')
        pa.godKill.play()


def elevenSound():
    if not pa.elevenKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('elevenKill playing')
        pa.elevenKill.play()


def twelveSound():
    if not pa.twelveKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('twelveKill playing')
        pa.twelveKill.play()


def thirteenSound():
    if not pa.thirteenKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('thirteenKill playing')
        pa.thirteenKill.play()


def fourteenSound():
    if not pa.fourteenKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('fourteenKill playing')
        pa.fourteenKill.play()


def fifteenSound():
    if not pa.fifteenKill.isPlaying:
        if logging == 'true':
            LOG_NOTE('fifteenKill playing')
        pa.fifteenKill.play()


def kamikaze():
    if logging == 'true':
        LOG_NOTE('kamikaze playing')
    pa.kamikazeSnd.play()


def ramkill():
    if logging == 'true':
        LOG_NOTE('ramkill playing')
    pa.ramkillSnd.play()


def bia():
    if not pa.biaSnd.isPlaying:
        if logging == 'true':
            LOG_NOTE('BiA playing')
        pa.biaSnd.play()


def crucial():
    if not pa.crucialSnd.isPlaying:
        if logging == 'true':
            LOG_NOTE('Crucial playing')
        pa.crucialSnd.play()


def denied():
    if not pa.deniedSnd.isPlaying:
        if logging == 'true':
            LOG_NOTE('Denied playing')
        pa.deniedSnd.play()


def payback():
    if logging == 'true':
        LOG_NOTE('Payback playing')
    pa.paybackSnd.play()


options = {1: firstone,
 2: double,
 3: triple,
 4: ultra,
 5: multi,
 6: monster,
 7: spree,
 8: rampage,
 9: nonstop,
 10: godlike,
 11: elevenSound,
 12: twelveSound,
 13: thirteenSound,
 14: fourteenSound,
 15: fifteenSound,
 20: ramkill,
 30: kamikaze,
 40: bia,
 50: crucial,
 60: denied,
 70: payback}

def killcheck(frags):
    if frags in options:
        options[frags]()


def stopSounds():
    if pa.firstBlood is None:
        return
    else:
        if pa.firstBlood.isPlaying or pa.sndDouble.isPlaying or hasattr(BigWorld.player().arena, 'firstbl') and BigWorld.player().arena.firstbl == True:
            if logging == 'true':
                LOG_NOTE('New Battle. Stopping all UT Sounds to play again.')
            pa.snd3min.stop()
            pa.snd2min.stop()
            pa.snd1min.stop()
            pa.snd30sec.stop()
            pa.snd10sec.stop()
            pa.sndDouble.stop()
            pa.sndFirstOne.stop()
            pa.firstBlood.stop()
            pa.sndTriple.stop()
            pa.ultraKill.stop()
            pa.multiKill.stop()
            pa.monsterKill.stop()
            pa.killingSpree.stop()
            pa.rampageKill.stop()
            pa.unstopKill.stop()
            pa.godKill.stop()
            pa.elevenKill.stop()
            pa.twelveKill.stop()
            pa.thirteenKill.stop()
            pa.fourteenKill.stop()
            pa.fifteenKill.stop()
            pa.kamikazeSnd.stop()
            pa.ramkillSnd.stop()
            pa.biaSnd.stop()
            pa.crucialSnd.stop()
            pa.deniedSnd.stop()
            pa.paybackSnd.stop()
        return
        return


def checkbuddy():
    ownID = BigWorld.player().arena.vehicles.get(BigWorld.player().playerVehicleID)['prebattleID']
    isCW = True if 'opponents' in BigWorld.player().arena.extraData else False
    if logging == 'true':
        LOG_NOTE('Players prebattleID is:', ownID)
        LOG_NOTE('Players own vehicle ID is:', BigWorld.player().playerVehicleID)
        if isCW:
            LOG_NOTE('CW match detected. Breaking off the search for platoon.')
    if isCW:
        return
    if BigWorld.player().arena.vehicles.get(BigWorld.player().playerVehicleID)['prebattleID'] != 0 and BigWorld.player().arena.UT_buddy1 == 0:
        for id, p in BigWorld.player().arena.vehicles.iteritems():
            if p['prebattleID'] == ownID and id != BigWorld.player().playerVehicleID:
                if BigWorld.player().arena.UT_buddy1 == 0:
                    BigWorld.player().arena.UT_buddy1 = id
                    if logging == 'true':
                        LOG_NOTE('Platoon Buddy 1:', id, p['name'])
                elif BigWorld.player().arena.UT_buddy2 == 0:
                    BigWorld.player().arena.UT_buddy2 = id
                    if logging == 'true':
                        LOG_NOTE('Platoon Buddy 2:', id, p['name'])


def removetext():
    if removeCallBackId is not None:
        BigWorld.cancelCallback(removeCallBackId)
    Battle.Battle._Battle__callEx(g_appLoader.getDefBattleApp(), 'timerBig.hide')
    return


def calltext():
    if g_appLoader.getDefBattleApp() is not None:
        if textCallBackId is not None:
            BigWorld.cancelCallback(textCallBackId)
        Battle.Battle._Battle__callEx(g_appLoader.getDefBattleApp(), 'timerBig.setTimer', [BigWorld.player().arena.UTtext])
        removeCallBackId = BigWorld.callback(delay, removetext)
    return


def calltextinit(newtext, targetID, attackerID, buddyID):
    if logging == 'true':
        LOG_NOTE('textinit:', newtext, targetID, attackerID, buddyID)
    BigWorld.player().arena.UTtemplate = Template(newtext)
    if buddyID is not None:
        try:
            BigWorld.player().arena.UTtext = BigWorld.player().arena.UTtemplate.safe_substitute(attacker=BigWorld.player().arena.vehicles.get(attackerID)['name'], target=BigWorld.player().arena.vehicles.get(targetID)['name'], buddy=BigWorld.player().arena.vehicles.get(buddyID)['name'])
        except:
            BigWorld.player().arena.UTtext = 'Welcome back!'

    else:
        try:
            BigWorld.player().arena.UTtext = BigWorld.player().arena.UTtemplate.safe_substitute(attacker=BigWorld.player().arena.vehicles.get(attackerID)['name'], target=BigWorld.player().arena.vehicles.get(targetID)['name'], buddy='')
        except:
            BigWorld.player().arena.UTtext = 'Welcome back!'

    if g_appLoader.getDefBattleApp() is not None:
        Battle.Battle._Battle__callEx(g_appLoader.getDefBattleApp(), 'timerBig.setTimer', [BigWorld.player().arena.UTtext])
    textCallBackId = BigWorld.callback(0.3, calltext)
    return


def checksquadkills(targetID, attackerID, equipmentID, reason):
    if logging == 'true':
        LOG_NOTE('Check Squad Kills:', targetID, attackerID, reason)
    cstats = BigWorld.player().arena._ClientArena__statistics
    if BigWorld.player().arena.vehicles.get(BigWorld.player().playerVehicleID)['prebattleID'] == 0 or 'opponents' in BigWorld.player().arena.extraData or BigWorld.player().arena.UT_buddy1 == 0:
        if logging == 'true':
            LOG_NOTE('Player not in a Platoon. Returning.')
        firstcheck(targetID, attackerID, equipmentID, reason, True, None)
        return
    else:
        if BigWorld.player().arena.UT_buddy2 != 0:
            squadfrags = cstats.get(BigWorld.player().playerVehicleID)['frags'] + cstats.get(BigWorld.player().arena.UT_buddy1)['frags'] + cstats.get(BigWorld.player().arena.UT_buddy2)['frags']
        else:
            squadfrags = cstats.get(BigWorld.player().playerVehicleID)['frags'] + cstats.get(BigWorld.player().arena.UT_buddy1)['frags']
        if logging == 'true':
            LOG_NOTE('Squadfrags:', squadfrags)
        if squadfrags >= 12:
            if logging == 'true':
                LOG_NOTE('Squadfrags >= 12')
            if not BigWorld.player().arena.Crucial:
                if showtext == 'true':
                    calltextinit(crucialtext, targetID, attackerID, None)
                if logging == 'true':
                    LOG_NOTE('Crucial detected!')
                BigWorld.player().arena.Crucial = True
                killcheck(50)
                return
            if logging == 'true':
                LOG_NOTE('Crucial already achieved.')
            firstcheck(targetID, attackerID, equipmentID, reason, True, None)
        if BigWorld.player().arena.BiA == False and not BigWorld.player().arena.BiAFail:
            if cstats.get(BigWorld.player().playerVehicleID)['frags'] >= 3 and cstats.get(BigWorld.player().arena.UT_buddy1)['frags'] >= 3:
                if logging == 'true':
                    LOG_NOTE('Two Platoonmates have each minimum 3 kills.')
                if BigWorld.player().arena.UT_buddy2 == 0:
                    if showtext == 'true':
                        calltextinit(biatext, targetID, attackerID, None)
                    if logging == 'true':
                        LOG_NOTE('BiA detected (2 Man platoon).')
                    BigWorld.player().arena.BiA = True
                    killcheck(40)
                if BigWorld.player().arena.UT_buddy2 != 0:
                    if cstats.get(BigWorld.player().arena.UT_buddy2)['frags'] >= 3:
                        if showtext == 'true':
                            calltextinit(biatext, targetID, attackerID, None)
                        if logging == 'true':
                            LOG_NOTE('BiA detected (3 Man).')
                        BigWorld.player().arena.BiA = True
                        killcheck(40)
                    else:
                        if logging == 'true':
                            LOG_NOTE('Buddy 2 not 3 kills.')
                        firstcheck(targetID, attackerID, equipmentID, reason, True, None)
            else:
                if logging == 'true':
                    LOG_NOTE('Player or Buddy 1 not 3 kills.')
                firstcheck(targetID, attackerID, equipmentID, reason, True, None)
        else:
            if logging == 'true':
                LOG_NOTE('None of the above Going back to firstcheck.')
            firstcheck(targetID, attackerID, reason, equipmentID, True, None)
        return
        return


def firstcheck(targetID, attackerID, equipmentID, reason, sqchecked, killerID):
    if not hasattr(BigWorld.player().arena, 'firstbl'):
        BigWorld.player().arena.firstbl = False
    if BigWorld.player().arena.firstbl == False:
        BigWorld.player().arena.firstbl = True
        if logging == 'true':
            LOG_NOTE('Firstblood playing from firstcheck function.')
        if firstoption == 'any':
            if showtext == 'true':
                calltextinit(firsttext, targetID, attackerID, None)
            pa.firstBlood.play()
        elif firstoption == 'me':
            if attackerID == BigWorld.player().playerVehicleID:
                if showtext == 'true':
                    calltextinit(firsttext, targetID, attackerID, None)
                pa.firstBlood.play()
    if killerID != None:
        if logging == 'true':
            LOG_NOTE('Player died to:', killerID)
        BigWorld.player().arena.BiAFail = True
        if BigWorld.player().arena.BiA:
            if showtext == 'true':
                calltextinit(deniedtext, targetID, killerID, None)
            if logging == 'true':
                LOG_NOTE('BiA denied Player died.')
            BigWorld.player().arena.BiA = False
            killcheck(60)
            return
    if targetID == BigWorld.player().arena.UT_buddy1:
        BigWorld.player().arena.UT_killer1 = attackerID
        if logging == 'true':
            LOG_NOTE('Buddy 1 died.')
        BigWorld.player().arena.BiAFail = True
        if logging == 'true':
            LOG_NOTE('Buddy 1 Killer ID:', attackerID)
        if BigWorld.player().arena.BiA:
            if showtext == 'true':
                calltextinit(deniedtext, targetID, attackerID, None)
            if logging == 'true':
                LOG_NOTE('BiA denied Buddy 1 died.')
            BigWorld.player().arena.BiA = False
            killcheck(60)
            return
    if BigWorld.player().arena.UT_buddy2 != 0 and targetID == BigWorld.player().arena.UT_buddy2:
        BigWorld.player().arena.UT_killer2 = attackerID
        if logging == 'true':
            LOG_NOTE('Buddy 2 died.')
        BigWorld.player().arena.BiAFail = True
        if logging == 'true':
            LOG_NOTE('Buddy 2 Killer ID:', attackerID)
        if BigWorld.player().arena.BiA:
            if showtext == 'true':
                calltextinit(deniedtext, targetID, attackerID, None)
            if logging == 'true':
                LOG_NOTE('BiA denied Buddy 2 died.')
            BigWorld.player().arena.BiA = False
            killcheck(60)
            return
    if BigWorld.player().arena.vehicles.get(targetID)['team'] == BigWorld.player().arena.vehicles.get(attackerID)['team']:
        if logging:
            LOG_NOTE('Teamkill. No need to do more.')
        return
    else:
        if (attackerID == BigWorld.player().playerVehicleID or attackerID == BigWorld.player().arena.UT_buddy1 or attackerID == BigWorld.player().arena.UT_buddy2) and not sqchecked:
            if logging == 'true':
                LOG_NOTE('Calling checksquadkills function.')
            checksquadkills(targetID, attackerID, equipmentID, reason)
        elif attackerID == BigWorld.player().playerVehicleID and targetID == BigWorld.player().arena.UT_killer1 or attackerID == BigWorld.player().arena.UT_buddy2 and targetID == BigWorld.player().arena.UT_killer1:
            if showtext == 'true':
                calltextinit(paybacktext, targetID, attackerID, BigWorld.player().arena.UT_buddy1)
            if logging == 'true':
                LOG_NOTE('Payback detected for Buddy 1!', targetID, attackerID)
            killcheck(70)
        elif attackerID == BigWorld.player().playerVehicleID and targetID == BigWorld.player().arena.UT_killer2 or attackerID == BigWorld.player().arena.UT_buddy1 and targetID == BigWorld.player().arena.UT_killer2:
            if showtext == 'true':
                calltextinit(paybacktext, targetID, attackerID, BigWorld.player().arena.UT_buddy2)
            if logging == 'true':
                LOG_NOTE('Payback detected for Buddy2!', targetID, attackerID)
            killcheck(70)
        elif attackerID == BigWorld.player().arena.UT_buddy1 and targetID == BigWorld.player().arena.UT_ownkiller:
            if showtext == 'true':
                calltextinit(paybackowntext, targetID, attackerID, BigWorld.player().arena.UT_buddy1)
            if logging == 'true':
                LOG_NOTE('Payback for dead player detected from Buddy1!', targetID, attackerID)
            killcheck(70)
        elif attackerID == BigWorld.player().arena.UT_buddy2 and targetID == BigWorld.player().arena.UT_ownkiller:
            if showtext == 'true':
                calltextinit(paybackowntext, targetID, attackerID, BigWorld.player().arena.UT_buddy2)
            if logging == 'true':
                LOG_NOTE('Payback for dead player detected from Buddy2!', targetID, attackerID)
            killcheck(70)
        elif attackerID == BigWorld.player().playerVehicleID and reason == 2:
            if BigWorld.player().arena.vehicles.get(attackerID)['vehicleType'].type.level < BigWorld.player().arena.vehicles.get(targetID)['vehicleType'].type.level:
                if showtext == 'true':
                    calltextinit(kamitext, targetID, attackerID, None)
                if logging == 'true':
                    LOG_NOTE('Kamikaze detected!', targetID, attackerID)
                killcheck(30)
            else:
                if showtext == 'true':
                    calltextinit(ramtext, targetID, attackerID, None)
                if logging == 'true':
                    LOG_NOTE('Ramkill detected!', targetID, attackerID)
                killcheck(20)
        elif attackerID == BigWorld.player().playerVehicleID and reason <= 1:
            cstats = BigWorld.player().arena._ClientArena__statistics
            frags = cstats.get(BigWorld.player().playerVehicleID)['frags']
            if logging == 'true':
                LOG_NOTE('Calling normal killcheck function.', targetID, attackerID)
                LOG_NOTE('Playerfrags:', frags)
            killcheck(frags)
        return
        return


old_AVK = ClientArena.ClientArena._ClientArena__onVehicleKilled

def newAVK(self, argStr):
	if BigWorld.player().arena is not None:
		import cPickle
		victimID, killerID, equipmentID, reason = cPickle.loads(argStr)
		if not hasattr(BigWorld.player().arena, 'BiA'):
			initial()
		if logging == 'true':
			LOG_NOTE('A Vehicle got Killed (targetID, attackerID, equipmentID, reason):', victimID, killerID, equipmentID, reason)
		checkbuddy()
		if pa.firstBlood is not None:
			firstcheck(victimID, killerID, equipmentID, reason, False, None)
	old_AVK(self, argStr)
        return


ClientArena.ClientArena._ClientArena__onVehicleKilled = newAVK

def checkownkiller():
    if BigWorld.player().arena.killerCallBackId is not None:
        BigWorld.cancelCallback(BigWorld.player().arena.killerCallBackId)
    killerID = BigWorld.player().inputHandler.getKillerVehicleID()
    BigWorld.player().arena.UT_ownkiller = killerID
    targetID = BigWorld.player().playerVehicleID
    if logging == 'true':
        LOG_NOTE('Player died. Calling firstcheck with following:', targetID, killerID, 0, True, killerID)
    firstcheck(targetID, killerID, equipmentID, 0, True, killerID)
    return


def checktime(arenaLength, period):
    if period != 3:
        stopSounds()
        initial()
        return
    if arenaLength == 180 and not pa.snd3min.isPlaying:
        pa.snd3min.play()
    elif arenaLength == 120 and not pa.snd2min.isPlaying:
        pa.snd2min.play()
    elif arenaLength == 60 and not pa.snd1min.isPlaying:
        pa.snd1min.play()
    elif arenaLength == 30 and not pa.snd30sec.isPlaying:
        pa.snd30sec.play()
    elif arenaLength == 10 and not pa.snd10sec.isPlaying:
        pa.snd10sec.play()


BigWorld.checktime = checktime
old_setTotalTime = TimersBar.setTotalTime

def newsetTotalTime(self, level, totalTime):
    if logging == 'true':
        print ('Set Total Time: ', level, totalTime)
    if hasattr(BigWorld, 'player'):
        if hasattr(BigWorld.player(), 'shop') or BigWorld.player().arena is None:
            old_setTotalTime(self, level, totalTime)
            
        if hasattr(BigWorld.player(), 'arena'):
            period = BigWorld.player().arena.period
            replayCtrl = BattleReplay.g_replayCtrl
            if replayCtrl.isPlaying:
                arenaLength = int(replayCtrl.getArenaLength())
            else:
                arenaLength = int(BigWorld.player().arena.periodEndTime - BigWorld.serverTime())
            BigWorld.checktime(arenaLength, period)
    old_setTotalTime(self, level, totalTime)


TimersBar.setTotalTime = newsetTotalTime

def __startBattleL(self):
    if logging == 'true':
        print 'startBattle'
    pa.firstBlood = WebiumSound(first)
    pa.sndFirstOne = WebiumSound(firstS)
    pa.sndDouble = WebiumSound(doubleS)
    pa.sndTriple = WebiumSound(tripleS)
    pa.ultraKill = WebiumSound(ultraS)
    pa.multiKill = WebiumSound(multiS)
    pa.monsterKill = WebiumSound(monsterS)
    pa.killingSpree = WebiumSound(spreeS)
    pa.rampageKill = WebiumSound(rampS)
    pa.unstopKill = WebiumSound(unstopS)
    pa.godKill = WebiumSound(godS)
    pa.elevenKill = WebiumSound(elevenS)
    pa.twelveKill = WebiumSound(twelveS)
    pa.thirteenKill = WebiumSound(thirteenS)
    pa.fourteenKill = WebiumSound(fourteenS)
    pa.fifteenKill = WebiumSound(fifteenS)
    pa.kamikazeSnd = WebiumSound(kamiS)
    pa.ramkillSnd = WebiumSound(ramkillS)
    pa.biaSnd = WebiumSound(biaS)
    pa.crucialSnd = WebiumSound(crucialS)
    pa.deniedSnd = WebiumSound(deniedS)
    pa.paybackSnd = WebiumSound(paybackS)
    pa.snd3min = WebiumSound(t3minsS)
    pa.snd2min = WebiumSound(t2minsS)
    pa.snd1min = WebiumSound(t1minS)
    pa.snd30sec = WebiumSound(t30secsS)
    pa.snd10sec = WebiumSound(t10secsS)

"""saved_a = Battle.afterCreate
def new_a(self):
saved_a(self)


Battle.afterCreate = new_a """

g_appLoader.onGUISpaceChanged += __startBattleL
old_onvehicleDestr = DamagePanelMeta.DamagePanelMeta.as_setVehicleDestroyedS

def newvehicleDestroyed(self):
    if not hasattr(BigWorld.player().arena, 'BiA'):
        initial()
        checkbuddy()
    BigWorld.player().arena.killerCallBackId = BigWorld.callback(0.5, checkownkiller)
    old_onvehicleDestr(self)


DamagePanelMeta.DamagePanelMeta.as_setVehicleDestroyedS = newvehicleDestroyed
