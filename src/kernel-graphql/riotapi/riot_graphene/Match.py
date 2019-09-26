from graphene import Boolean, Field, Int, List, String

from riotwatcher import RiotWatcher, ApiError

from .RiotGrapheneObject import RiotGrapheneObject


class MatchPosition(RiotGrapheneObject):
    y = Int()
    x = Int()


class MatchParticipantFrame(RiotGrapheneObject):
    totalGold = Int()
    teamScore = Int()
    participantId = Int()
    level = Int()
    currentGold = Int()
    minionsKilled = Int()
    dominionScore = Int()
    position = Field(MatchPosition)
    xp = Int()
    jungleMinionsKilled = Int()


class MatchEvent(RiotGrapheneObject):
    eventType = String()
    towerType = String()
    teamId = Int()
    ascendedType = String()
    killerId = Int()
    levelUpType = String()
    pointCaptured = String()
    assistingParticipantIds = List(Int)
    wardType = String()
    monsterType = String()
    type = String()  # todo: enum
    skillSlot = Int()
    victimId = Int()
    timestamp = Int()
    afterId = Int()
    monsterSubType = String()
    laneType = String()
    itemId = Int()
    participantId = Int()
    buildingType = String()
    creatorId = Int()
    position = Field(MatchPosition)
    beforeId = Int()


class MatchFrame(RiotGrapheneObject):
    timestamp = Int()
    # participantFrames = Map(String, MatchParticipantFrame)
    events = List(MatchEvent)


class MatchTimeline(RiotGrapheneObject):
    frames = List(MatchFrame)
    frameInterval = Int()


class Player(RiotGrapheneObject):
    currentPlatformId = String()
    summonerName = String()
    matchHistoryUri = String()
    platformId = String()
    currentAccountId = String()
    profileIcon = Int()
    summonerId = String()
    accountId = String()

    summoner = Field(lambda: Summoner)

    def resolve_summoner(self, info):
        watcher: RiotWatcher = info.context

        summ = watcher.summoner.by_id(self.region, self.summonerId)

        return Summoner(self.region, summ)


class Rune(RiotGrapheneObject):
    runeId = Int()
    rank = Int()


class Mastery(RiotGrapheneObject):
    masteryId = Int()
    rank = Int()


class ParticipantStats(RiotGrapheneObject):
    firstBloodAssist = Boolean()
    visionScore = Int()
    magicDamageDealtToChampions = Int()
    damageDealtToObjectives = Int()
    totalTimeCrowdControlDealt = Int()
    longestTimeSpentLiving = Int()
    perk1Var1 = Int()
    perk1Var3 = Int()
    perk1Var2 = Int()
    tripleKills = Int()
    perk3Var3 = Int()
    nodeNeutralizeAssist = Int()
    perk3Var2 = Int()
    playerScore9 = Int()
    playerScore8 = Int()
    kills = Int()
    playerScore1 = Int()
    playerScore0 = Int()
    playerScore3 = Int()
    playerScore2 = Int()
    playerScore5 = Int()
    playerScore4 = Int()
    playerScore7 = Int()
    playerScore6 = Int()
    perk5Var1 = Int()
    perk5Var3 = Int()
    perk5Var2 = Int()
    totalScoreRank = Int()
    neutralMinionsKilled = Int()
    damageDealtToTurrets = Int()
    physicalDamageDealtToChampions = Int()
    nodeCapture = Int()
    largestMultiKill = Int()
    perk2Var2 = Int()
    perk2Var3 = Int()
    totalUnitsHealed = Int()
    perk2Var1 = Int()
    perk4Var1 = Int()
    perk4Var2 = Int()
    perk4Var3 = Int()
    wardsKilled = Int()
    largestCriticalStrike = Int()
    largestKillingSpree = Int()
    quadraKills = Int()
    teamObjective = Int()
    magicDamageDealt = Int()
    item2 = Int()
    item3 = Int()
    item0 = Int()
    neutralMinionsKilledTeamJungle = Int()
    item6 = Int()
    item4 = Int()
    item5 = Int()
    perk1 = Int()
    perk0 = Int()
    perk3 = Int()
    perk2 = Int()
    perk5 = Int()
    perk4 = Int()
    perk3Var1 = Int()
    damageSelfMitigated = Int()
    magicalDamageTaken = Int()
    firstInhibitorKill = Boolean()
    trueDamageTaken = Int()
    nodeNeutralize = Int()
    assists = Int()
    combatPlayerScore = Int()
    perkPrimaryStyle = Int()
    goldSpent = Int()
    trueDamageDealt = Int()
    participantId = Int()
    totalDamageTaken = Int()
    physicalDamageDealt = Int()
    sightWardsBoughtInGame = Int()
    totalDamageDealtToChampions = Int()
    physicalDamageTaken = Int()
    totalPlayerScore = Int()
    win = Boolean()
    objectivePlayerScore = Int()
    totalDamageDealt = Int()
    item1 = Int()
    neutralMinionsKilledEnemyJungle = Int()
    deaths = Int()
    wardsPlaced = Int()
    perkSubStyle = Int()
    turretKills = Int()
    firstBloodKill = Boolean()
    trueDamageDealtToChampions = Int()
    goldEarned = Int()
    killingSprees = Int()
    unrealKills = Int()
    altarsCaptured = Int()
    firstTowerAssist = Boolean()
    firstTowerKill = Boolean()
    champLevel = Int()
    doubleKills = Int()
    nodeCaptureAssist = Int()
    inhibitorKills = Int()
    firstInhibitorAssist = Boolean()
    perk0Var1 = Int()
    perk0Var2 = Int()
    perk0Var3 = Int()
    visionWardsBoughtInGame = Int()
    altarsNeutralized = Int()
    pentaKills = Int()
    totalHeal = Int()
    totalMinionsKilled = Int()
    timeCCingOthers = Int()


class ParticipantTimeline(RiotGrapheneObject):
    lane = String()
    participantId = Int()
    # TODO
    # csDiffPerMinDeltas
    # goldPerMinDeltas
    # xpDiffPerMinDeltas
    # creepsPerMinDeltas
    # xpPerMinDeltas
    role = String()
    # damageTakenDiffPerMinDeltas
    # damageTakenPerMinDeltas


class Participant(RiotGrapheneObject):
    stats = Field(ParticipantStats)
    participantId = Int()
    runes = List(Rune)
    timeline = Field(ParticipantTimeline)
    teamId = Int()
    spell2Id = Int()
    masteries = List(Mastery)
    highestAchievedSeasonTier = String()
    spell1Id = Int()
    championId = Int()


class ParticipantIdentity(RiotGrapheneObject):
    player = Field(Player)
    participantId = Int()


class TeamBans(RiotGrapheneObject):
    pickTurn = Int()
    championId = Int()


class TeamStats(RiotGrapheneObject):
    firstDragon = Boolean()
    firstInhibitor = Boolean()
    bans = List(TeamBans)
    baronKills = Int()
    firstRiftHerald = Boolean()
    firstBaron = Boolean()
    riftHeraldKills = Int()
    firstBlood = Boolean()
    teamId = Int()
    firstTower = Boolean()
    vilemawKills = Int()
    inhibitorKills = Int()
    towerKills = Int()
    dominionVictoryScore = Int()
    win = String()
    dragonKills = Int()


class Match(RiotGrapheneObject):
    seasonId = Int()
    queueId = Int()
    gameId = String()
    participantIdentities = List(ParticipantIdentity)
    gameVersion = String()
    platformId = String()
    gameMode = String()
    mapId = Int()
    gameType = String()
    teams = List(TeamStats)
    participants = List(Participant)
    gameDuration = Int()
    gameCreation = String()  # TODO: use datetime instead

    timeline = Field(MatchTimeline)

    def resolve_timeline(self, info):
        watcher: RiotWatcher = info.context

        try:
            timeline = watcher.match.timeline_by_match(self.region, self.gameId)

            return MatchTimeline(self.region, timeline)
        except ApiError as e:
            if e.response.status_code == 404:
                return None
            raise


class MatchReference(RiotGrapheneObject):
    lane = String()
    gameId = String()
    champion = Int()
    platformId = String()
    season = Int()
    queue = Int()
    role = String()
    timestamp = String()

    match = Field(Match)

    def resolve_match(self, info):
        watcher: RiotWatcher = info.context

        match = watcher.match.by_id(self.region, self.gameId)

        return Match(self.region, match)


class Matchlist(RiotGrapheneObject):
    matches = List(MatchReference)
    totalGames = Int()
    startIndex = Int()
    endIndex = Int()


from .Summoner import Summoner
