from flask.ext.babel import lazy_gettext

LICENSE_MAP = (
    ('', lazy_gettext('Select a License')),
    ('cc_zero', lazy_gettext('Creative Commons Zero - Public Domain')),
    ('cc_by', lazy_gettext('Creative Commons Attribution')),
    ('cc_by_sa', lazy_gettext('Creative Commons Attribution Share Alike')),
    ('cc_by_nd', lazy_gettext('Creative Commons Attribution No Derivatives'))
)

LANGUAGES = [
    ('', lazy_gettext('Select a Language')),
        ('eng', lazy_gettext('English')),
        ('ger', lazy_gettext('German')),
        ('fre', lazy_gettext('French')),
        ('rus', lazy_gettext('Russian')),
        ('spa', lazy_gettext('Spanish')),
        ('ita', lazy_gettext('Italian')),
        ('jpn', lazy_gettext('Japanese')),
        ('lat', lazy_gettext('Latin')),
        ('zhn', lazy_gettext('Chinese')),
        ('dut', lazy_gettext('Dutch')),
        ('tur', lazy_gettext('Turkish')),
        ('por', lazy_gettext('Portuguese')),
        ('pol', lazy_gettext('Polish')),
        ('gre', lazy_gettext('Greek')),
        ('srp', lazy_gettext('Serbian')),
        ('cat', lazy_gettext('Catalan')),
        ('dan', lazy_gettext('Danish')),
        ('cze', lazy_gettext('Czech')),
        ('kor', lazy_gettext('Korean')),
        ('ara', lazy_gettext('Arabic')),
        ('hun', lazy_gettext('Hungarian')),
        ('swe', lazy_gettext('Swedish')),
        ('ukr', lazy_gettext('Ukranian')),
        ('heb', lazy_gettext('Hebrew')),
        ('hrv', lazy_gettext('Croatian')),
        ('slo', lazy_gettext('Slovak')),
        ('nor', lazy_gettext('Norwegian')),
        ('rum', lazy_gettext('Romanian')),
        ('fin', lazy_gettext('Finnish')),
        ('geo', lazy_gettext('Georgian')),
        ('bul', lazy_gettext('Bulgarian')),
        ('grc', lazy_gettext('Ancient Greek')),
        ('ind', lazy_gettext('Indonesian Language')),
        ('gmh', lazy_gettext('Middle High German')),
        ('mon', lazy_gettext('Mongolian Language')),
        ('peo', lazy_gettext('Persian')),
        ('alb', lazy_gettext('Albanian')),
        ('bos', lazy_gettext('Bosnian')),
    ]

USER_ROLES = [
    ('', lazy_gettext('Select a Role')),
    ('aut', lazy_gettext('Author')),
    ('aui', lazy_gettext('Author of Foreword')),
    ('ive', lazy_gettext('Interviewee')),
    ('ivr', lazy_gettext('Interviewer')),
    ('trl', lazy_gettext('Translator')),
    ('ths', lazy_gettext('Thesis Advisor')),
    ('ctb', lazy_gettext('Contributor')),
    ('edt', lazy_gettext('Editor')),
    ('inv', lazy_gettext('Inventor')),
    ('prg', lazy_gettext('Programmer')),
    ('drt', lazy_gettext('Director')),
    ('spk', lazy_gettext('Speaker')),
    ('cmp', lazy_gettext('Composer')),
]

CORP_ROLES = [
    ('', lazy_gettext('Select a Role')),
    ('ctb', lazy_gettext('Contributor')),
    ('edt', lazy_gettext('Editor')),
    ('his', lazy_gettext('Host institution')),
    ('dgg', lazy_gettext('Degree granting institution')),
    ('orm', lazy_gettext('Organizer')),
    ('pta', lazy_gettext('Patent applicant')),
    ('brd', lazy_gettext('Broadcaster')),
]

ADMIN_ROLES = USER_ROLES[:]

ADMIN_ROLES.extend([
    ('abr', lazy_gettext('Abridger')),
    ('act', lazy_gettext('Actor')),
    ('aft', lazy_gettext('Author of Afterword')),
    ('arr', lazy_gettext('Arranger')),
    ('chr', lazy_gettext('Choreographer')),
    ('cmp', lazy_gettext('Composer')),
    ('cst', lazy_gettext('Costume Designer')),
    ('cwt', lazy_gettext('Commentator for written text')),
    ('elg', lazy_gettext('Electrician')),
    ('fmk', lazy_gettext('Filmmaker')),
    ('hnr', lazy_gettext('Honoree')),
    ('ill', lazy_gettext('Illustrator')),
    ('itr', lazy_gettext('Instrumentalist')),
    ('mod', lazy_gettext('Moderator')),
    ('mus', lazy_gettext('Musician')),
    ('org', lazy_gettext('Originator')),
    ('pdr', lazy_gettext('Project Director')),
    ('pht', lazy_gettext('Photographer')),
    ('pmn', lazy_gettext('Production Manager')),
    ('pro', lazy_gettext('Producer')),
    ('red', lazy_gettext('Redaktor')),
    ('sng', lazy_gettext('Singer')),
    ('std', lazy_gettext('Set designer')),
    ('stl', lazy_gettext('Storyteller')),
    ('tcd', lazy_gettext('Technical Director')),
    ])

USER_PUBTYPES = [
    ('', lazy_gettext('Select a Publication Type')),
    ('ArticleJournal', lazy_gettext('Article in Journal')),
    ('Chapter', lazy_gettext('Chapter in...')),
    ('Collection', lazy_gettext('Collection')),
    ('MultivolumeWork', lazy_gettext('MultivolumeWork')),
    ('Monograph', lazy_gettext('Monograph')),
    ('Other', lazy_gettext('Other')),
    ('Report', lazy_gettext('Report')),
    ('Patent', lazy_gettext('Patent')),
    ('Thesis', lazy_gettext('Thesis')),
    ('Software', lazy_gettext('Software')),
    ('ResearchData', lazy_gettext('Research Data')),
]

ADMIN_PUBTYPES = USER_PUBTYPES[:]

ADMIN_PUBTYPES.extend([
    ('ArticleNewspaper', lazy_gettext('Article in Newspaper')),
    ('AudioVideoDocument', lazy_gettext('Audio or Video Document')),
    ('ChapterInLegalCommentary', lazy_gettext('Chapter in a Legal Commentary')),
    ('Conference', lazy_gettext('Conference')),
    ('Edition', lazy_gettext('Edition')),
    ('InternetDocument', lazy_gettext('Internet Document')),
    ('Journal', lazy_gettext('Journal')),
    ('Lecture', lazy_gettext('Lecture')),
    ('LegalCommentary', lazy_gettext('Legal Commentary')),
    ('Newspaper', lazy_gettext('Newspaper')),
    ('PressRelease', lazy_gettext('Press Release')),
    ('RadioTVProgram', lazy_gettext('Radio or TV program')),
    ('Series', lazy_gettext('Series')),
    ('SpecialIssue', lazy_gettext('Special Issue')),
    ('Standard', lazy_gettext('Standard')),
])

EDITORIAL_STATUS = [
    ('', lazy_gettext('Select an Editorial Status')),
    ('new', lazy_gettext('New')),
    ('in_process', lazy_gettext('Editing')),
    ('processed', lazy_gettext('Edited')),
    ('final_editing', lazy_gettext('Final Editing')),
    ('finalized', lazy_gettext('Finalized')),
    ('imported', lazy_gettext('Imported')),
    ('deleted', lazy_gettext('Deleted')),
]

PERS_STATUS_MAP = [
    ('', lazy_gettext('Select a Status')),
    ('alumnus', lazy_gettext('Alumnus')),
    ('assistant_lecturer', lazy_gettext('Assistant Lecturer')),
    ('callcenter', lazy_gettext('Callcenter')),
    ('ranking', lazy_gettext('Relevant for Ranking')),
    ('external', lazy_gettext('External Staff')),
    ('manually_added', lazy_gettext('Manually added')),
    ('official', lazy_gettext('Official')),
    ('official_ns', lazy_gettext('Official, Non-Scientific')),
    ('research_school', lazy_gettext('Doctoral Candidate')),
    ('principal_investigator', lazy_gettext('Principal Investigator')),
    ('professor', lazy_gettext('Professor')),
    ('emeritus', lazy_gettext('Emeritus')),
    ('teaching_assistant', lazy_gettext('Teaching Assistant')),
    ('tech_admin', lazy_gettext('Technical and Administrative Staff')),
]

PROJECT_TYPES = [
    ('', lazy_gettext('Select a Project Type')),
    ('fp7', lazy_gettext('FP7')),
    ('h2020', lazy_gettext('Horizon 2020')),
    ('dfg', lazy_gettext('DFG')),
    ('mercur', lazy_gettext('Mercator Research Center Ruhr (MERCUR)')),
    ('other', lazy_gettext('Other')),
]

CARRIER = [
    ('', lazy_gettext('Select a Carrier')),
    ('AudioDisc', lazy_gettext('Audio disc')),
    ('Audiocassette', lazy_gettext('Audiocassette')),
    ('AudiotapeReel', lazy_gettext('Audiotape reel')),
    ('ComputerDisc', lazy_gettext('Computer disc')),
    ('OnlineRessource', lazy_gettext('Online-ressource')),
    ('Microfiche', lazy_gettext('Microfiche')),
    ('MicrofilmCassette', lazy_gettext('Microfilm cassette')),
    ('MicrofilmReel', lazy_gettext('Microfilm reel')),
    ('MicrofilmRoll', lazy_gettext('Microfilm roll')),
    ('MicroscopeSlide', lazy_gettext('Microscope slide')),
    ('FilmCassette', lazy_gettext('Film cassette')),
    ('FilmReel', lazy_gettext('Film reel')),
    ('FilmRoll', lazy_gettext('Film roll')),
    ('FilmStrip', lazy_gettext('Film strip')),
    ('Object', lazy_gettext('Object')),
    ('card', lazy_gettext('card')),
    ('Videocassette', lazy_gettext('Videocassette')),
    ('Videodisc', lazy_gettext('Videodisc')),
    ('Unspecified', lazy_gettext('Unspecified')),
]

RESOURCE_TYPES = [
    ('', lazy_gettext('Select a Resource Type')),
    ('Audiovisual', lazy_gettext('Audiovisual')),
    ('Collection', lazy_gettext('Collection')),
    ('Dataset', lazy_gettext('Dataset')),
    ('Event', lazy_gettext('Event')),
    ('Image', lazy_gettext('Image')),
    ('InteractiveResource', lazy_gettext('InteractiveResource')),
    ('Model', lazy_gettext('Model')),
    ('PhysicalObject', lazy_gettext('PhysicalObject')),
    ('Service', lazy_gettext('Service')),
    ('Software', lazy_gettext('Software')),
    ('Sound', lazy_gettext('Sound')),
    ('Text', lazy_gettext('Text')),
    ('Workflow', lazy_gettext('Workflow')),
    ('Other', lazy_gettext('Other')),
]

FREQUENCY = [
    ('', lazy_gettext('Select a Frequency')),
    ('completely_irregular', lazy_gettext('Completely Irregular')),
    ('annual', lazy_gettext('Annual')),
    ('quarterly', lazy_gettext('Quarterly')),
    ('semiannual', lazy_gettext('Semiannual')),
    ('monthly', lazy_gettext('Monthly')),
    ('bimonthly', lazy_gettext('Bimonthly')),
    ('three_times_a_year', lazy_gettext('Three Times a Year')),
    ('semimonthly', lazy_gettext('Semimonthly')),
    ('biennial', lazy_gettext('Biannial')),
    ('fifteen_issues_a_year', lazy_gettext('Fifteen Issues a Year')),
    ('continuously_updated', lazy_gettext('Continuously Updated')),
    ('daily', lazy_gettext('Daily')),
    ('semiweekly', lazy_gettext('Semiweekly')),
    ('three_times_a_week', lazy_gettext('Three Times a Week')),
    ('weekly', lazy_gettext('Weekly')),
    ('biweekly', lazy_gettext('Biweekly')),
    ('three_times_a_month', lazy_gettext('Three Times a Month')),
    ('triennial', lazy_gettext('Triennial')),
]

PUB_STATUS = [
    ('', lazy_gettext('Select a Publication Status')),
    ('published', lazy_gettext('Published')),
    ('unpublished', lazy_gettext('Unpublished'))
]

CATALOGS = [
    ('Ruhr-Universität Bochum', lazy_gettext('Ruhr-Universität Bochum')),
    ('Technische Universität Dortmund', lazy_gettext('Technische Universität Dortmund')),
    ('Temporäre Daten', lazy_gettext('Temporäre Daten')),
]

