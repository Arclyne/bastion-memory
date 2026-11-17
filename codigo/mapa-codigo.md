---
tipo: mapa-codigo
generado: sí (herramientas/mapa_codigo.py; no editar a mano; ver herramientas/LEEME.md)
---
# Mapa del código

Formato. proyectos: `Proyecto | framework | ref:proyectos | paq:paquetes`. tipos: `Nombre TipoLíneas | miembros públicos` (C clase, R record, I interfaz, E enum, S struct; `~` interno; `+N` = N más sin listar). contratos: `Operación(parámetros) -> retorno [oneway] !fallas`. tablas: `Tabla | script | columnas`. Qué hace cada proyecto: [[sistemas]]. Valores: [[valores]]. Qué caso de uso usa cada cosa: `python3 herramientas/ver.py casos`.

# huella
repo=bastion commit=6dfb198 rama=main generado=2026-11-17
huella: archivos=679 lineas=42486 codigo=9d292511 sql=a24c8a31
# solucion
Bastion.slnx
# proyectos
Bastion.Client.Networking | heredado | ref:Bastion.Contracts | paq:System.ServiceModel.NetTcp,System.ServiceModel.Primitives,log4net
Bastion.Client | heredado | ref:Bastion.Client.Networking,Bastion.Domain | paq:Gum.MonoGame,Gum.Shapes.MonoGame,KernSmith.MonoGameGum,MonoGame.Content.Builder.Task,MonoGame.Framework.DesktopGL,log4net
Bastion.Contracts | netstandard2.0 | ref:- | paq:System.ServiceModel.Primitives
Bastion.Domain | heredado | ref:- | paq:-
Bastion.Server.Adapters | heredado | ref:Bastion.Domain,Bastion.Server.Application | paq:Microsoft.EntityFrameworkCore.SqlServer,log4net
Bastion.Server.Application | heredado | ref:Bastion.Domain | paq:log4net
Bastion.Server.Host | heredado | ref:Bastion.Contracts,Bastion.Server.Adapters,Bastion.Server.Application | paq:CoreWCF.ConfigurationManager,CoreWCF.NetTcp,CoreWCF.Primitives,Microsoft.Extensions.Logging.Log4Net.AspNetCore,log4net
Bastion.Client.Tests | heredado | ref:Bastion.Client,Bastion.Client.Networking,Bastion.Contracts | paq:-
Bastion.Domain.Tests | heredado | ref:Bastion.Domain | paq:-
Bastion.Server.Application.Tests | heredado | ref:Bastion.Server.Application | paq:-
# pruebas
Bastion.Client.Tests | clases=17 pruebas=182
Bastion.Domain.Tests | clases=20 pruebas=171
Bastion.Server.Application.Tests | clases=19 pruebas=243
# contratos
## IAccountService
LogIn(credentials,device) -> PlayerSession !InvalidCredentialsFault,AccountRestrictedFault
## IChatService
SendChatMessage(sessionToken,text) -> ChatMessageReceipt !InvalidSessionFault,ChatMessageRejectedFault
OpenLobbyChat(sessionToken) -> LobbyChatLog !InvalidSessionFault
SendMatchChatMessage(sessionToken,matchId,text) -> ChatMessageReceipt !InvalidSessionFault,ChatChannelForbiddenFault,ChatMessageRejectedFault
## IFriendshipService
ListFriends(sessionToken) -> FriendList !InvalidSessionFault
SearchPlayers(sessionToken,text) -> PlayerSearchEntry[] !InvalidSessionFault
SendFriendRequest(sessionToken,friendCode) -> FriendRequestResult !InvalidSessionFault,FriendshipRejectedFault
ListFriendRequests(sessionToken) -> FriendRequestList !InvalidSessionFault
AcceptFriendRequest(sessionToken,requesterFriendCode) -> void !InvalidSessionFault,FriendshipRejectedFault
RejectFriendRequest(sessionToken,requesterFriendCode) -> void !InvalidSessionFault,FriendshipRejectedFault
CancelFriendRequest(sessionToken,recipientFriendCode) -> void !InvalidSessionFault,FriendshipRejectedFault
RemoveFriend(sessionToken,friendCode) -> void !InvalidSessionFault,FriendshipRejectedFault
## IMatchService
AbandonMatch(sessionToken,matchId) -> void !InvalidSessionFault,MatchNotJoinedFault
MovePawn(sessionToken,move) -> void !InvalidSessionFault,MatchNotJoinedFault,NotYourTurnFault,IllegalMoveFault
PlaceWall(sessionToken,wall) -> void !InvalidSessionFault,MatchNotJoinedFault,NotYourTurnFault,IllegalWallFault
## IMatchmakingService
StartSearch(sessionToken) -> void !InvalidSessionFault,SearchRejectedFault
CancelSearch(sessionToken) -> void oneway
ConfirmPresence(sessionToken) -> void oneway
## INotificationCallback
ReceiveNotification(notification) -> void oneway
## IConversationService
ListConversations(sessionToken) -> ConversationEntry[] !InvalidSessionFault
OpenConversation(sessionToken,friendCode) -> PrivateConversationLog !InvalidSessionFault,ChatMessageRejectedFault
SendPrivateMessage(sessionToken,friendCode,text) -> ChatMessageReceipt !InvalidSessionFault,ChatMessageRejectedFault
MarkConversationRead(sessionToken,friendCode) -> void !InvalidSessionFault,ChatMessageRejectedFault
## IRoomService
CreateRoom(sessionToken,options) -> RoomState !InvalidSessionFault,RoomRejectedFault
JoinRoom(sessionToken,code) -> RoomState !InvalidSessionFault,RoomRejectedFault
SetReady(sessionToken,isReady) -> RoomState !InvalidSessionFault,RoomRejectedFault
ChangeOptions(sessionToken,options) -> RoomState !InvalidSessionFault,RoomRejectedFault
StartMatch(sessionToken) -> void !InvalidSessionFault,RoomRejectedFault
LeaveRoom(sessionToken) -> void oneway
FindOwnRoom(sessionToken) -> RoomState? !InvalidSessionFault
## ISessionService
Subscribe(sessionToken) -> void !InvalidSessionFault
KeepAlive() -> void oneway
# tipos
## Bastion.Client
BastionGame C236
Program C34 | Main
## Bastion.Client.Controls
CountBadge C32
LanguagePicker C43
ModalLayer C35
NoticeBox C123
PasswordField C20
TabButton C38
TextField C20
## Bastion.Client.Localization
ILanguagePreferenceStore I8 | LoadCultureName,SaveCultureName
ILanguageService I39 | ChangeLanguage,LoadInitialLanguage
LanguageCatalog C51 | FindByCultureName,FindClosest
LanguagePreferenceStore C77 | LoadCultureName,SaveCultureName
LanguageService C135 | ChangeLanguage,LoadInitialLanguage
SupportedLanguage R24 | ToString
## Bastion.Client.Networking
ServerConnection C86 | Dispose
## Bastion.Client.Networking.Accounts
AccountClient C93 | LogIn
AccountRestrictedException C17
AccountRestriction E9 | Locked,Pending,Suspended,Banned
IAccountClient I6 | LogIn
InvalidCredentialsException C28
LoggedInSession C23
LoginCredentials C19
## Bastion.Client.Networking.Channels
ChannelCloser C40 | CloseOrAbort
ChannelSettings C45 | ApplyCertificateValidation,CreateAddress,CreateBinding
ConnectionLostException C28
DeviceIdentity C27 | GetClientVersion,GetFingerprint
IServiceChannel I11 | Call
ISessionChannelFactory I8 | CreateChannel
ServerAddress C48 | Create,GetCertificateThumbprint
ServerErrorException C28
ServerUnreachableException C28
ServiceChannel C60 | Call,Dispose
ServiceFailureTranslator C29 | ToClientException
SessionChannelFactory C34 | CreateChannel,Dispose
ThumbprintX509CertificateValidator C33 | Validate
## Bastion.Client.Networking.Chat
ChatAuthor R18
ChatChannelForbiddenException C28
ChatClient C85 | OpenLobbyChat,SendMatchChatMessage,SendMessage
ChatContractTranslator C79 | ToChatMessage,ToMessageRejectedException,ToRejection,ToTranscript
ChatMessage R22
ChatMessageRejectedException C17
ChatMute R5
ChatRejection E11 | InvalidMessage,Muted,BannedTerm,TooFast,NotFriends,PlayerNotFound
IChatClient I15 | OpenLobbyChat,SendMatchChatMessage,SendMessage
LobbyChatTranscript R23
## Bastion.Client.Networking.Friends
FoundPlayer R18
FriendClient C124 | AcceptFriendRequest,CancelFriendRequest,ListFriendRequests,ListFriends,RejectFriendRequest,RemoveFriend,SearchPlayers,SendFriendRequest
FriendContractTranslator C165 | ToFoundPlayers,ToFriendListing,ToFriendRequestListing,ToListedFriend,ToOutcome,ToPendingRequest,ToPlayerTag,ToRejection
FriendListing R23
FriendPresence E7 | Connected,Disconnected
FriendRelationship E10 | None,RequestSent,RequestReceived,AlreadyFriends,OwnAccount
FriendRequestListing R26
FriendRequestOutcome E7 | RequestSent,FriendshipStarted
FriendshipRejectedException C14
FriendshipRejection E13 | PlayerNotFound,OwnAccount,AlreadyFriends,RequestAlreadySent,FriendLimitReached,RecipientFriendLimitReached,RequestNotFound,NotFriends
IFriendClient I22 | AcceptFriendRequest,CancelFriendRequest,ListFriendRequests,ListFriends,RejectFriendRequest,RemoveFriend,SearchPlayers,SendFriendRequest
ListedFriend R21
PendingFriendRequest R21
PlayerTag R19
## Bastion.Client.Networking.Matches
ChosenPawnMove R21
ChosenWall R12
IMatchClient I19 | AbandonMatch,MovePawn,PlaceWall
IllegalMoveException C28
IllegalWallException C17
MatchClient C111 | AbandonMatch,MovePawn,PlaceWall
MatchContractTranslator C101 | ToIllegalWallException,ToWallPlacedEventArgs,ToWallPlacement
MatchNotJoinedException C28
NotYourTurnException C17
PlacedWallOrientation E7 | Horizontal,Vertical
WallPlacementRejection E9 | NoWallsLeft,OutOfBoard,GrooveTaken,WouldBlockPlayer
## Bastion.Client.Networking.Matchmaking
IMatchmakingClient I21 | CancelSearch,ConfirmPresence,StartSearch
MatchmakingClient C109 | CancelSearch,ConfirmPresence,StartSearch
SearchEndReason E8 | Cancelled,PresenceExpired,MatchCreationFailed
SearchRejectedException C14
SearchRejection E8 | NotificationsUnavailable,UnfinishedMatch,InRoom
## Bastion.Client.Networking.Notifications
ChatMessageReceivedEventArgs C16
FoundMatchFormat R3
FoundMatchParticipant R21
FriendPresenceChangedEventArgs C19
FriendRequestReceivedEventArgs C16
FriendshipStartedEventArgs C16
INotificationClient I40 | Connect,Disconnect
MatchAbandonedEventArgs C21
MatchChatMessageReceivedEventArgs C19
MatchFoundEventArgs C23
NotificationCallback C392 | ReceiveNotification
NotificationClient C233 | Connect,Disconnect,Dispose
PawnMovedEventArgs C22
PresenceRequestedEventArgs C13
PrivateMessageReceivedEventArgs C21
RoomClosedEventArgs C19
RoomUpdatedEventArgs C16
SearchEndedEventArgs C14
WallPlacedEventArgs C23
## Bastion.Client.Networking.PrivateChat
ConversationClient C94 | ListConversations,MarkConversationRead,OpenConversation,SendMessage
ConversationContact R19
ConversationContractTranslator C63 | ToPreviews,ToPrivateMessage,ToSender,ToTranscript
ConversationPreview R22
ConversationTranscript R25
IConversationClient I15 | ListConversations,MarkConversationRead,OpenConversation,SendMessage
PrivateMessage R21
## Bastion.Client.Networking.Rooms
IRoomClient I27 | ChangeOptions,CreateRoom,FindOwnRoom,JoinRoom,LeaveRoom,SetReady,StartMatch
PrivateRoom R14
PrivateRoomGameMode E8 | Classic,FourPlayers,Quick
PrivateRoomMember R12
PrivateRoomOptions R3
RoomClient C146 | ChangeOptions,CreateRoom,FindOwnRoom,JoinRoom,LeaveRoom,SetReady,StartMatch
RoomCloseReason E6 | HostLeft
RoomContractTranslator C130 | ToCloseReason,ToPrivateRoom,ToRejection,ToRoomOptions
RoomRejectedException C17
RoomRejection E19 | NotificationsUnavailable,UnfinishedMatch,SearchingMatch,InRoom,InvalidOptions,RoomNotFound,RoomFull,Kicked,TooManyAttempts,TooManyPlayers,NotInRoom,NotHost,NotReadyToStart,MatchStarted
## Bastion.Client.Networking.Sessions
InvalidSessionException C28
## Bastion.Client.Platform
GumClipboard C28 | TryCopyText
GumScreenHost C76 | ShowScreen
## Bastion.Client.Screens
BadgeText C18 | FormatCount
DialogCard C28
IClipboard I6 | TryCopyText
IEscapeKeyReceiver I6 | ReceiveEscapeKey
INavigator I10 | ShowLogin,ShowMainMenu
IScreenHost I6 | ShowScreen
LocalServices R24
NoticeTone E9 | None,Error,Warning,Success
ScreenNavigator C172 | Dispose,ReceiveEscapeKey,ShowLogin,ShowMainMenu
ScreenView C33
UiThread C20 | Run
ViewFactory C184 | CenterHorizontally,CenterVertically,ClearRows,CreateBoundLabel,CreateBoundNotice,CreateBoundUntranslatedLabel,CreateButton,CreateLabel,CreateScrollList,CreateUntranslatedLabel,CreateVersionLabel,RequireRow
## Bastion.Client.Screens.Login
LoginView C285
LoginViewModel C337 | CloseDialog,LogIn,RetryLogIn
ServerFailureDialogView C86
## Bastion.Client.Screens.MainMenu
BadgeBinding R19
MainMenuView C389 | ReceiveEscapeKey
MainMenuViewModel C63 | ConnectNotifications
MatchSearchPanel C55
MatchSearchStage E8 | Idle,Searching,MatchFound
MatchSearchViewModel C369 | CancelSearch,ConfirmPresence,Dispose,StartSearch
PresenceDialogView C51
## Bastion.Client.Screens.MainMenu.Chat
ChatChannelListView C176
ChatClients R26
ChatComposerViewModel C100
ChatContext R24
ChatMessageRowView C69 | CreateVisual
ChatMessageRowViewModel C31 | CreatePending
ChatPane E8 | List,Global,Private
ChatRejectionText C57 | Describe,DescribeInvalidMessage,DescribeMute
ChatTabView C37
ChatTabViewModel C270 | BackToList,Dispose,Load,LoadConversations,OpenGlobal,OpenPrivate,RefreshPresence
ChatTimeText C66 | DescribeDay,DescribeLastActivity,FormatMoment,FormatTime,GetLocalDay,GetLocalToday
ConversationParts C113 | CreateHeader,CreateInputRow,CreateMessageList,CreateNoticeLabel,CreateWrappedLabel,ScrollToLatest
ConversationPresence R18
ConversationRowView C105
ConversationRowViewModel C67 | ShowMessage,UpdateUnread
ConversationUpdatedEventArgs C21
IFriendDirectory I6 | FindPresence
LobbyChatView C148
LobbyChatViewModel C282 | CloseConversation,Dispose,LoadChannel,OpenConversation,SendMessage,UpdateReadingPosition
MessageRowViewModel C70 | Confirm,Fail
PrivateConversationView C166
PrivateConversationViewModel C392 | ApplyPresence,Close,IsShowing,Load,Open,Receive,SendMessage
PrivateMessageRowView C126 | CreateVisual
PrivateMessageRowViewModel C35 | CreatePending,HasDayLabel
## Bastion.Client.Screens.MainMenu.Friends
AddFriendView C115
AddFriendViewModel C200 | Reset,SearchPlayers,SendRequest
FoundPlayerRowView C68
FoundPlayerRowViewModel C74 | ApplyOutcome,MarkRequestSent
FriendActionsMenu C84
FriendActionsViewModel C175 | AskRemoval,CloseAll,ConfirmRemoval,OpenMenu,RequestMessage
FriendCodeFooter C46
FriendListView C158
FriendRejectionText C33 | Describe
FriendRemovedEventArgs C15
FriendRequestRowView C126
FriendRequestRowViewModel C68
FriendRequestToast C96
FriendRequestsView C98
FriendRequestsViewModel C378 | Accept,AcceptToast,Cancel,LoadRequests,ReceiveRequest,Reject,RejectToast,ShowReceived,ShowSent
FriendRowView C97
FriendRowViewModel C45
FriendsPanel C178
FriendsPanelViewModel C415 | Close,CloseAddFriend,CopyOwnCode,Dispose,FindPresence,LoadFriends,Open,OpenAddFriend,SelectTab
FriendsTab E8 | Friends,Requests,Chat
LastSeenText C44 | DescribeLastSeen
MessageRequestedEventArgs C16
RemoveFriendDialogView C92
SocialClients R26
## Bastion.Client.Screens.Matches
BoardPawn R19
JoinedMatch R34 | FindOwnParticipant,IsOwnParticipant
JoinedMatchViewModels R26
MatchAbandonmentViewModel C198 | AbandonMatch,Dispose,RequestReturnToMenu
MatchChatPanel C95
MatchChatViewModel C140 | Dispose,SendMessage
MatchPlayViewModel C431 | BuildBoard,CanPlaceWall,ClearSelection,Dispose,FindNickname,GetRemainingWalls,IsOwnTurn,PlaceWall,SelectSquare
MatchPlayerViewModel C77 | HideTurn,MarkLeft,ShowTurn,ShowWalls
MatchPlayersPanel C122
MatchScreenText C36 | FormatClock,FormatElo,FormatMode,FormatWallCount
MatchView C166
MatchViewModel C188 | Dispose
MatchWallTranslator C57 | ToPlacedWallOrientation,ToRejectionReason,ToWallOrientation
PlayerLeftEventArgs C15
RivalAbandonedDialogView C41
VersusPlayer R23
VersusView C106
VersusViewModel C107 | Dispose
WallControlsPanel C107
WallPlacementViewModel C210 | Cancel,ChooseGroove,ClearHover,Confirm,Dispose,HoverGroove,Rotate,Start
WallRejectionText C28 | Describe
## Bastion.Client.Screens.Matches.Scene
BoardScene C332 | Dispose,Draw,TryFindGrooveUnderCursor,TryFindSquareUnderCursor
BoardSceneLayout C145 | GetCameraPosition,GetCellCenter,GetGoalMeshName,GetWallTransform,IsGoalMesh,TryGetCoordinates,TryGetGroove
SceneCamera R5
SceneModel C84 | DrawMesh,TintMesh
WallMesh C55 | Draw
## Bastion.Client.Theme
ButtonLook R32
ButtonLookCatalog C66
ButtonSkin C111 | CreateAndAttach,ShowState
CardSkin C42 | Apply
DialogMetrics C14
FieldSkin C96 | CreateAndAttach,ShowState
FontCatalog C9
InteractionFlags E14 | None,Hovered,Pressed,Focused,Disabled,Checked
InteractiveSkin C80 | ShowState
Palette C111 | GetPawnColor
PanelMetrics C6
PickerSkin C115 | CreateAndAttach,ShowState
ScreenMetrics C8
ShapeFactory C76 | CreateCircle,CreateHalo,CreateRounded,HideDefaultParts,InsertBehindContent
SkinState C22 | Show
TextStyle R42 | ApplyTo
TextStyleCatalog C56
ThemeInitializer C38 | Initialize
## Bastion.Contracts
ServiceEndpoints C42 | CreateAddress,IsRegisteredPort
## Bastion.Contracts.Accounts
AccountRestrictedFault C13
ClientDevice C13
IAccountService I30 | LogIn
InvalidCredentialsFault C8
PlayerCredentials C13
PlayerSession C16
RestrictionReason E19 | Locked,Pending,Suspended,Banned
## Bastion.Contracts.Chat
ChatChannelForbiddenFault C8
ChatMessageReceipt C14
ChatMessageRejectedFault C14
ChatRejectionReason E25 | InvalidMessage,Muted,BannedTerm,TooFast,NotFriends,PlayerNotFound
IChatService I70 | OpenLobbyChat,SendChatMessage,SendMatchChatMessage
LobbyChatLog C20
LobbyChatMessage C23
## Bastion.Contracts.Friends
FriendList C17
FriendListEntry C20
FriendRequestEntry C20
FriendRequestList C17
FriendRequestResult E13 | RequestSent,FriendshipStarted
FriendshipRejectedFault C10
FriendshipRejectionReason E31 | PlayerNotFound,OwnAccount,AlreadyFriends,RequestAlreadySent,FriendLimitReached,RecipientFriendLimitReached,RequestNotFound,NotFriends
IFriendshipService I147 | AcceptFriendRequest,CancelFriendRequest,ListFriendRequests,ListFriends,RejectFriendRequest,RemoveFriend,SearchPlayers,SendFriendRequest
PlayerRelationship E22 | NotRelated,RequestSent,RequestReceived,Friends,Self
PlayerSearchEntry C16
PresenceState E13 | Connected,Disconnected
## Bastion.Contracts.Matches
IMatchService I91 | AbandonMatch,MovePawn,PlaceWall
IllegalMoveFault C8
IllegalWallFault C13
MatchNotJoinedFault C8
NotYourTurnFault C13
PawnMove C16
WallOrientation E13 | Horizontal,Vertical
WallPlacement C19
WallRejectionReason E19 | NoWallsLeft,OutOfBoard,GrooveTaken,WouldBlockPlayer
## Bastion.Contracts.Matchmaking
IMatchmakingService I45 | CancelSearch,ConfirmPresence,StartSearch
SearchRejectedFault C10
SearchRejectionReason E16 | NotificationsUnavailable,UnfinishedMatch,InRoom
## Bastion.Contracts.Notifications
ChatMessageNotification C16
FriendPresenceNotification C21
FriendRequestNotification C17
FriendshipStartedNotification C13
INotificationCallback I18 | ReceiveNotification
MatchAbandonedNotification C16
MatchChatMessageNotification C19
MatchFoundNotification C22
MatchFoundParticipant C16
Notification C25
PawnMovedNotification C31
PresenceRequestedNotification C11
PrivateMessageNotification C19
RoomClosedNotification C13
RoomClosedReason E10 | HostLeft
RoomUpdatedNotification C11
SearchEndedNotification C10
SearchEndedReason E16 | Cancelled,PresenceExpired,MatchCreationFailed
WallPlacedNotification C32
## Bastion.Contracts.PrivateChat
ConversationEntry C22
IConversationService I85 | ListConversations,MarkConversationRead,OpenConversation,SendPrivateMessage
PrivateChatMessage C20
PrivateConversationLog C26
## Bastion.Contracts.Rooms
IRoomService I124 | ChangeOptions,CreateRoom,FindOwnRoom,JoinRoom,LeaveRoom,SetReady,StartMatch
RoomGameMode E16 | Classic,FourPlayers,Quick
RoomMemberState C19
RoomOptions C16
RoomRejectedFault C13
RoomRejectionReason E49 | NotificationsUnavailable,UnfinishedMatch,SearchingMatch,InRoom,InvalidOptions,RoomNotFound,RoomFull,Kicked,TooManyAttempts,TooManyPlayers,NotInRoom,NotHost,NotReadyToStart,MatchStarted
RoomState C19
## Bastion.Contracts.Sessions
ISessionService I27 | KeepAlive,Subscribe
InvalidSessionFault C8
## Bastion.Domain.Accounts
Account C141 | Activate,ChangePassword,GetRemainingLockMinutes,HasPassword,IsLockedAt,RecordFailedLogin,RecordLastSeen,RecordSuccessfulLogin
AccountPolicy C41 | IsValidEmail,IsValidLoginIdentifier,IsValidNickname
AccountStatus E10 | Pending,Active,Suspended,Banned,Deleted
AccountType E7 | Registered,Guest
LockoutPolicy C36 | GetLockDuration
## Bastion.Domain.Auditing
AccessAttempt R23
AccessLog C34
AccessLogResult E11 | LoginSucceeded,AccountNotFound,AccountLocked,WrongPassword,AccountPending,AccountSanctioned
## Bastion.Domain.Chat
ChatPolicy C19 | IsValidMessage
ChatWordFilter C59 | HasBannedTerm
MatchChatSubmission R18
Message C82 | CreateForMatch,CreatePrivate,GetPartnerId,IsSentBy,MarkRead
MessageChannel E10 | Match,Spectators,Room,Global,Friends
MessageParticipants R3
## Bastion.Domain.Friends
FriendCodePolicy C52 | Format,IsValid,Normalize
FriendRequest C45 | GetExpirationTime,IsExpiredAt,IsSentBy
Friendship C30
FriendshipPolicy C7
## Bastion.Domain.GameModes
GameMode C16
GameModeCode E8 | Classic,FourPlayers,Quick
## Bastion.Domain.Matches
Board R112 | GetPawnCoordinates,HasWall,IsBlocked,IsInside,IsOccupied,ListTurnOrders,WithWall
BoardCoordinates R3
BoardLayout C119 | GetLastIndex,GetStartingCoordinates,GetStartingSquare,IsGoal,ParseSquare,ToSquare,TryParseSquare
BoardStep R54 | Advance,GetOpposite,IsBetweenRows
Match C392 | Abandon,BuildBoard,CanBeAbandonedBy,FindWallRejection,GetNextMoveNumber,GetParticipation,IsPlayedBy,IsTurnOf,ListReachableSquares,MovePawn,PlaceWall,StartPrivate,StartRanked
MatchEndReason E10 | Goal,Timeout,Resignation,Draw,Abandonment
MatchEntrant R3
MatchFormat R22
MatchStatus E8 | InProgress,PendingClose,Finished
MatchType E7 | Ranked,Private
Move C74 | GetDestination,GetWall
MoveTiming R5
MoveType E7 | PawnMove,Wall
Participation C126 | GetPawnSymbol,HasWallsLeft
ParticipationResult E8 | Won,Lost,Draw
PawnMove R21
PawnMovePolicy C72 | ListReachableSquares
PawnSymbol E9 | Blue,Red,Green,Yellow
Wall R18
WallOrientation E7 | Horizontal,Vertical
WallPlacement R21
WallPolicy C115 | FindRejection
WallRejection R3
WallRejectionReason E9 | NoWallsLeft,OutOfBoard,GrooveTaken,WouldBlockPlayer
## Bastion.Domain.Matchmaking
MatchSearch C86 | ConfirmPresence,Equals,GetHashCode,HasPresenceExpired,IsSearching,ShouldStartPresenceCheck,StartPresenceCheck
MatchmakingPolicy C18
SearchStatus E7 | Searching,AwaitingPresence
## Bastion.Domain.Moderation
BannedWord C15
BannedWordScope E8 | Nickname,Chat,Both
Sanction C47 | IsInEffectAt,IsPermanent
SanctionScope E7 | Account,Chat
## Bastion.Domain.Rooms
FailedCodeAttemptHistory C53 | GetRetryDelay,HasAttempts,IsLimitReached,Record
Room C109 | ChangeSettings,Close,FinishMatch,Open,StartMatch
RoomIdentity R18
RoomMember C32
RoomOpening R21
RoomPolicy C45 | IsValidClock,IsValidCode,IsValidWallCount,NormalizeCode
RoomSettings R29 | IsValid
RoomStatus E8 | Open,InMatch,Closed
WaitingRoom C151 | Admit,CanSeatAllMembers,ChangeSettings,HasKicked,IsFull,IsHost,IsReadyToStart,Remove,SetReady
## Bastion.Domain.Sessions
ClientConnection R25
Session C56 | IsActiveAt
SessionTicket R18
## Bastion.Domain.Statistics
ModeStatistic C16
## Bastion.Domain.Text
TextPattern C19 | Create
## Bastion.Server.Adapters
AdaptersRegistration C41 | AddBastionAdapters
## Bastion.Server.Adapters.Matchmaking
TurnOrderShuffler C18 | ShuffleTurnOrder
## Bastion.Server.Adapters.Persistence
BastionDbContext C55
DatabaseFailureTranslator C36 | Run
DeletedRowCount C6
NewContextRunner C34 | Run
UnitOfWork C52 | SaveChanges
## Bastion.Server.Adapters.Persistence.Configurations
AccessLogConfiguration C24 | Configure
AccountConfiguration C40 | Configure
BannedWordConfiguration C23 | Configure
EnumColumnMapping C38 | HasUpperSnakeCaseConversion
FriendRequestConfiguration C17 | Configure
FriendshipConfiguration C22 | Configure
GameModeConfiguration C21 | Configure
MatchConfiguration C35 | Configure
MessageConfiguration C25 | Configure
ModeStatisticConfiguration C17 | Configure
MoveConfiguration C29 | Configure
ParticipationConfiguration C27 | Configure
RoomConfiguration C26 | Configure
SanctionConfiguration C23 | Configure
SessionConfiguration C27 | Configure
## Bastion.Server.Adapters.Persistence.Conversions
UpperSnakeCaseEnumConverter C42
## Bastion.Server.Adapters.Persistence.Repositories
AccessLogRepository C24 | Add
AccountRepository C100 | FindById,FindByLoginIdentifier,FindPlayerIdentity,FindPlayerIdentityByFriendCode,ListPlayerIdentities,SearchPlayerIdentities
BannedWordRepository C27 | ListChatTerms
FriendRequestRepository C119 | Add,FindBetween,ListInvolving,ListReceived,ListSent,Remove
FriendshipRepository C77 | Add,ListFriendAccountIds,ListFriends,Remove
MatchRepository C205 | FindAccountIdsWithUnfinishedParticipation,FindActiveGameMode,FindEloRatingsByAccountId,FindGameMode,FindMatch,HasUnfinishedParticipation,SaveAbandonment,SaveMatch,SaveMatchChatMessage,SaveMove
MessageRepository C93 | Add,CountUnreadByAuthor,ListConversation,ListLatestPerPartner,MarkRead
RoomRepository C138 | AddRoom,ChangeRoomSettings,CloseOpenRooms,CloseRoom,IsCodeTaken,IsRoomInMatch,SaveRoomMatch
SanctionRepository C29 | ListChatSanctions
SessionRepository C32 | Add,FindByTokenHash
## Bastion.Server.Adapters.Rooms
RoomCodeGenerator C13 | CreateCode
## Bastion.Server.Adapters.Security
PasswordHasher C53 | IsPasswordCorrect,SimulatePasswordCheck
SessionTokenGenerator C28 | Generate,Hash
## Bastion.Server.Application.Accounts
AccountRestrictedException C24
AccountRestriction E9 | Locked,Pending,Suspended,Banned
IAccountRepository I19 | FindById,FindByLoginIdentifier,FindPlayerIdentity,FindPlayerIdentityByFriendCode,ListPlayerIdentities,SearchPlayerIdentities
ILoginService I23 | LogIn
InvalidCredentialsException C23
LoggedInPlayer R23
LoginService C139 | LogIn
PlayerIdentity R30 | FromAccount
## Bastion.Server.Application.Auditing
IAccessLogRepository I8 | Add
## Bastion.Server.Application.Chat
ChatChannelForbiddenException C23
ChatCooldown C26 | TryStartCooldown
ChatHistoryEntry R18
ChatLine R23
ChatMessageRejectedException C24
ChatModerator C52 | FindMute,ScreenMessage
ChatMute R29 | FromSanctionsInEffect
ChatRejection E11 | InvalidMessage,Muted,BannedTerm,TooFast,NotFriends,PlayerNotFound
IChatBroadcaster I8 | Broadcast,CountListeners
IChatModerator I10 | FindMute,ScreenMessage
ILobbyChatRoom I15 | CountListeners,ListRecent,Post,TryStartCooldown
ILobbyChatService I39 | OpenLobbyChat,SendMessage
IMatchChatNotifier I8 | NotifyMatchChatMessage
IMatchChatRelay I13 | ListParticipantAccountIds,Post,TryStartCooldown
IMatchChatService I33 | SendMessage
LobbyChatHistory R23
LobbyChatRoom C64 | CountListeners,ListRecent,Post,TryStartCooldown
LobbyChatService C57 | OpenLobbyChat,SendMessage
MatchChatRelay C45 | ListParticipantAccountIds,Post,TryStartCooldown
MatchChatService C60 | SendMessage
PostedChatLine R18
## Bastion.Server.Application.Common
IPlayerActivity I10 | HasNotificationChannel,IsInRoom,IsSearchingMatch
IUnitOfWork I29 | SaveChanges
PlayerActivity C41 | HasNotificationChannel,IsInRoom,IsSearchingMatch
## Bastion.Server.Application.Friends
FriendCodeLookup C22 | FindPlayer
FriendListService C71 | ListFriends,RemoveFriend
FriendPresence E7 | Connected,Disconnected
FriendPresenceChange R22
FriendPresenceService C62 | ReportConnected,ReportDisconnected
FriendRelationship E10 | None,RequestSent,RequestReceived,AlreadyFriends,OwnAccount
FriendRelationshipResolver C57 | Resolve
FriendRequestBoard R26
FriendRequestOutcome E7 | RequestSent,FriendshipStarted
FriendRequestService C226 | AcceptFriendRequest,CancelFriendRequest,ListFriendRequests,RejectFriendRequest,SearchPlayers,SendFriendRequest
FriendRequestSummary R22
FriendRoster R23
FriendStatus R18
FriendSummary R19
FriendshipRejectedException C14
FriendshipRejection E13 | PlayerNotFound,OwnAccount,AlreadyFriends,RequestAlreadySent,FriendLimitReached,RecipientFriendLimitReached,RequestNotFound,NotFriends
IFriendListService I34 | ListFriends,RemoveFriend
IFriendNotifier I13 | NotifyFriendRequestReceived,NotifyFriendshipStarted,NotifyPresenceChanged
IFriendPresenceService I23 | ReportConnected,ReportDisconnected
IFriendRequestRepository I19 | Add,FindBetween,ListInvolving,ListReceived,ListSent,Remove
IFriendRequestService I99 | AcceptFriendRequest,CancelFriendRequest,ListFriendRequests,RejectFriendRequest,SearchPlayers,SendFriendRequest
IFriendshipRepository I15 | Add,ListFriendAccountIds,ListFriends,Remove
IPlayerPresence I6 | IsPlayerConnected
PlayerSearchResult R19
## Bastion.Server.Application.Matches
AbandonmentNotice R18
ChosenPawnMove R21
ChosenWall R14
IMatchAbandonmentService I23 | AbandonMatch
IMatchEndNotifier I8 | NotifyMatchAbandoned
IMatchMoveNotifier I10 | NotifyPawnMoved,NotifyWallPlaced
IMatchMoveService I56 | MovePawn,PlaceWall
IMatchRepository I29 | FindAccountIdsWithUnfinishedParticipation,FindActiveGameMode,FindEloRatingsByAccountId,FindGameMode,FindMatch,HasUnfinishedParticipation,SaveAbandonment,SaveMatch,SaveMatchChatMessage,SaveMove
IllegalMoveException C23
IllegalWallException C18
MatchAbandonmentService C59 | AbandonMatch
MatchMoveService C223 | MovePawn,PlaceWall
MatchNotJoinedException C23
MatchRepositoryException C28
NotYourTurnException C18
PawnMoveNotice R18
WallPlacementNotice R20
## Bastion.Server.Application.Matchmaking
CreatedMatch R24
CreatedMatchParticipant R22
IMatchSearchService I40 | CancelSearch,ConfirmPresence,StartSearch
IMatchmakingDispatcher I8 | ReviewAndNotify
IMatchmakingNotifier I12 | HasNotificationChannel,NotifyMatchFound,NotifyPresenceRequested,NotifySearchEnded
IMatchmakingPlayerVerifier I11 | VerifyPlayerCanSearch,VerifySession
IMatchmakingQueue I17 | ConfirmPresence,IsSearching,Review,TryAdd,TryRemove
IRankedMatchCreator I13 | TryCreateMatch
ITurnOrderShuffler I8 | ShuffleTurnOrder
MatchPairing R17
MatchSearchService C60 | CancelSearch,ConfirmPresence,StartSearch
MatchmakingDispatcher C63 | ReviewAndNotify
MatchmakingPlayerVerifier C57 | VerifyPlayerCanSearch,VerifySession
MatchmakingQueue C106 | ConfirmPresence,IsSearching,Review,TryAdd,TryRemove
PresenceRequest R5
QueueReview R28
RankedMatchCreator C106 | TryCreateMatch
SearchEndReason E8 | Cancelled,PresenceExpired,MatchCreationFailed
SearchRejectedException C14
SearchRejection E8 | NotificationsUnavailable,UnfinishedMatch,InRoom
## Bastion.Server.Application.Moderation
IBannedWordRepository I8 | ListChatTerms
ISanctionRepository I9 | ListChatSanctions
## Bastion.Server.Application.PrivateChat
ConversationPartner R19
ConversationSummary R22
IMessageRepository I18 | Add,CountUnreadByAuthor,ListConversation,ListLatestPerPartner,MarkRead
IPrivateChatRoom I10 | Deliver,TryStartCooldown
IPrivateChatService I72 | ListConversations,MarkConversationRead,OpenConversation,SendPrivateMessage
IPrivateMessageNotifier I6 | NotifyPrivateMessage
PrivateChatChannel R20
PrivateChatRoom C29 | Deliver,TryStartCooldown
PrivateChatService C152 | ListConversations,MarkConversationRead,OpenConversation,SendPrivateMessage
PrivateConversation R28
PrivateMessageDelivery R21
PrivateMessageDraft R19
PrivateMessageEntry R19
## Bastion.Server.Application.Rooms
IPrivateMatchCreator I9 | CreateMatch
IPrivateRoomService I81 | ChangeSettings,CreateRoom,FindOwnRoom,JoinRoom,LeaveRoom,SetReady
IRoomCodeGenerator I6 | CreateCode
IRoomKeeper I22 | ChangeSettings,CloseRoomsLeftOpen,FindRoomOf,Join,Leave,Open,SetReady
IRoomMatchService I27 | StartMatch
IRoomMatchStarter I9 | StartMatch
IRoomNotifier I8 | NotifyRoomClosed,NotifyRoomUpdated
IRoomPlayerVerifier I11 | VerifyPlayerCanEnterRoom,VerifySession
IRoomRegistry I27 | Admit,ChangeSettings,CreateUnusedCode,FindHostedRoom,FindRoomOf,IsInRoom,Leave,SetReady,StartMatch,TryOpen
IRoomRepository I22 | AddRoom,ChangeRoomSettings,CloseOpenRooms,CloseRoom,IsCodeTaken,IsRoomInMatch,SaveRoomMatch
IRoomSettingsValidator I8 | Validate
PrivateMatchCreator C71 | CreateMatch
PrivateRoomService C87 | ChangeSettings,CreateRoom,FindOwnRoom,JoinRoom,LeaveRoom,SetReady
RequestedRoomSettings R5
RoomDeparture R21
RoomKeeper C138 | ChangeSettings,CloseRoomsLeftOpen,FindRoomOf,Join,Leave,Open,SetReady
RoomMatchService C31 | StartMatch
RoomMatchStarter C33 | StartMatch
RoomMemberSnapshot R14
RoomPlayerVerifier C59 | VerifyPlayerCanEnterRoom,VerifySession
RoomRegistry C247 | Admit,ChangeSettings,CreateUnusedCode,FindHostedRoom,FindRoomOf,IsInRoom,Leave,SetReady,StartMatch,TryOpen
RoomRejectedException C22
RoomRejection E19 | NotificationsUnavailable,UnfinishedMatch,SearchingMatch,InRoom,InvalidSettings,RoomNotFound,RoomFull,Kicked,TooManyAttempts,TooManyPlayers,NotInRoom,NotHost,NotReadyToStart,MatchStarted
RoomRepositoryException C28
RoomSettingsValidator C37 | Validate
RoomSnapshot R68 | CanSeatAllMembers,Capture,GetSeatCount,ListAccountIdsExcept
## Bastion.Server.Application.Security
GeneratedToken R19
IPasswordHasher I8 | IsPasswordCorrect,SimulatePasswordCheck
ISessionTokenGenerator I8 | Generate,Hash
## Bastion.Server.Application.Sessions
ConnectedPlayer R18
ISessionRepository I10 | Add,FindByTokenHash
ISessionVerifier I11 | Verify,VerifyIdentity
InvalidSessionException C23
SessionVerifier C51 | Verify,VerifyIdentity
## Bastion.Server.Host
Program C107 | Main
ServerCertificate C54 | ApplyTo,Dispose,Load
ServiceRegistration C111 | AddBastionApplication,AddBastionHost,AddBastionServices
## Bastion.Server.Host.Accounts
AccountService C84 | LogIn
LoginTranslator C80 | ToAttempt,ToConnection,ToFault,ToSession
## Bastion.Server.Host.Chat
ChatService C120 | OpenLobbyChat,SendChatMessage,SendMatchChatMessage
ChatTranslator C123 | RequireText,ToChatLog,ToFault,ToLobbyChatNotification,ToMatchChatNotification,ToReceipt
## Bastion.Server.Host.Common
CallerAddress C22 | GetCurrent
ContractArray C21 | ConvertAll
FaultExceptionFactory C17 | Create
## Bastion.Server.Host.Friends
FriendPresenceReporter C71 | ReportConnected,ReportDisconnected
FriendshipService C212 | AcceptFriendRequest,CancelFriendRequest,ListFriendRequests,ListFriends,RejectFriendRequest,RemoveFriend,SearchPlayers,SendFriendRequest
FriendshipTranslator C203 | ToFault,ToFriendList,ToFriendRequestList,ToFriendRequestResult,ToFriendshipStartedNotification,ToPresenceNotification,ToRequestNotification,ToSearchEntries
IFriendPresenceReporter I8 | ReportConnected,ReportDisconnected
## Bastion.Server.Host.Matches
MatchService C134 | AbandonMatch,MovePawn,PlaceWall
MatchTranslator C188 | ToAbandonedNotification,ToChosenPawnMove,ToChosenWall,ToFault,ToPawnMovedNotification,ToUnreadableWallFault,ToWallPlacedNotification
## Bastion.Server.Host.Matchmaking
MatchmakingBackgroundService C35
MatchmakingService C133 | CancelSearch,ConfirmPresence,StartSearch
MatchmakingTranslator C100 | ToFault,ToMatchFoundNotification,ToPresenceRequestedNotification,ToSearchEndedNotification
## Bastion.Server.Host.PrivateChat
ConversationService C155 | ListConversations,MarkConversationRead,OpenConversation,SendPrivateMessage
PrivateChatTranslator C87 | ToConversationEntries,ToConversationLog,ToPrivateMessageNotification,ToReceipt
## Bastion.Server.Host.Rooms
RoomCleanupService C75 | StartAsync,StopAsync
RoomService C239 | ChangeOptions,CreateRoom,FindOwnRoom,JoinRoom,LeaveRoom,SetReady,StartMatch
RoomTranslator C155 | ToClosedNotification,ToFault,ToRequestedSettings,ToState,ToUpdatedNotification
## Bastion.Server.Host.Sessions
INotificationChannelRegistry I12 | RegisterChannel
NotificationChannelRegistry C291 | Broadcast,CountListeners,HasNotificationChannel,IsPlayerConnected,NotifyFriendRequestReceived,NotifyFriendshipStarted,NotifyMatchAbandoned,NotifyMatchChatMessage,NotifyMatchFound,NotifyPawnMoved,NotifyPresenceChanged,NotifyPresenceRequested,NotifyPrivateMessage,NotifyRoomClosed,+4
PlayerDisconnectedEventArgs C13
SessionService C77 | KeepAlive,Subscribe
SessionTranslator C23 | RequireSessionToken,ToFault
# base de datos
scripts: 01_create_database.sql,02_create_tables.sql,03_insert_test_data.sql,04_insert_leaderboard_demo.sql,05_create_friends.sql,06_insert_chat_test_data.sql,07_create_private_messages.sql
## tablas
AccessLog | 02_create_tables.sql | AccessLogId,AccountId,EnteredIdentifier,Result,IpAddress,OccurredAt
Account | 02_create_tables.sql | AccountId,AccountType,AccountStatus,Role,Nickname,Email,PasswordHash,PasswordSalt,BirthDate,PreferredLanguage,FailedAttempts,LastFailedAttemptAt,LockedUntil,IsTwoFactorEnabled,RegisteredAt,LastVerificationSentAt,LastRecoverySentAt,TermsVersion,TermsLanguage,TermsAcceptedAt,DeletedAt
Appeal | 02_create_tables.sql | AppealId,SanctionId,Text,HasFlaggedLanguage,SubmittedAt,Status,ModeratorId,AssignedAt,ResolutionNote,ResolvedAt
BannedWord | 02_create_tables.sql | BannedWordId,Term,Language,Scope
Block | 02_create_tables.sql | BlockerId,BlockedId,BlockedAt
DrawOffer | 02_create_tables.sql | DrawOfferId,MatchId,OffererId,MoveNumber,OfferedAt,Status,RespondedAt
FriendRequest | 05_create_friends.sql | RequesterId,RecipientId,RequestedAt,PairLowId,PairHighId
Friendship | 05_create_friends.sql | AccountAId,AccountBId,BefriendedAt
GameMode | 02_create_tables.sql | GameModeId,Code,BoardSize,PlayerCount,WallsPerPlayer,IsActive
Match | 02_create_tables.sql | MatchId,GameModeId,MatchType,Status,ClockMinutes,StartedAt,EndedAt,EndReason,CurrentTurn
Message | 02_create_tables.sql | MessageId,AuthorId,Channel,MatchId,RoomId,Text,SentAt
ModeStatistic | 02_create_tables.sql | AccountId,GameModeId,EloRating,LastMatchAt,MatchesPlayed,MatchesWon,MatchesLost,Abandonments
ModerationLog | 02_create_tables.sql | ModerationLogId,ModeratorId,Action,AffectedAccountId,Detail,OccurredAt
Move | 02_create_tables.sql | MatchId,MoveNumber,AccountId,MoveType,FromSquare,ToSquare,Groove,Orientation,TimeSpent,PlayedAt
Mute | 02_create_tables.sql | AccountId,MutedId,MutedAt
Participation | 02_create_tables.sql | MatchId,AccountId,TurnOrder,PawnSymbol,CurrentSquare,RemainingWalls,RemainingClock,InitialElo,FinalElo,EloChange,Result,Placement,EndReason,IsConnected,DisconnectedAt,IsFinished
Report | 02_create_tables.sql | ReportId,ReporterId,ReportedId,Reason,Description,MatchId,SubmittedAt,Status,ModeratorId,AssignedAt,ResolutionNote,ResolvedAt
Room | 02_create_tables.sql | RoomId,Code,HostId,GameModeId,WallsPerPlayer,ClockMinutes,Status,MatchId,CreatedAt,LastActivityAt
Sanction | 02_create_tables.sql | SanctionId,AccountId,ModeratorId,ReportId,Scope,SanctionType,Reason,StartedAt,EndedAt,RevokedAt,ReplacementSanctionId,IsActive
Session | 02_create_tables.sql | SessionId,AccountId,TokenHash,StartedAt,ExpiresAt,LastUsedAt,EndedAt,CloseReason,IpAddress,DeviceFingerprint,DeviceName,ClientVersion
VerificationCode | 02_create_tables.sql | VerificationCodeId,AccountId,Purpose,CodeHash,TargetEmail,IssuedAt,ExpiresAt,Attempts,Status
## procedimientos
usp_Block_Apply | 02_create_tables.sql
usp_Block_Delete | 02_create_tables.sql
usp_FriendRequest_Delete | 05_create_friends.sql
usp_Friendship_Delete | 05_create_friends.sql
usp_Mute_Delete | 02_create_tables.sql
usp_Room_Close | 02_create_tables.sql
