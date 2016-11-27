import uuid
from chatterbot.queues import ResponseQueue


class Session(object):
    """
    A single chat session.
    """

    def __init__(self):
        # A unique identifier for the chat session
        self.uuid = uuid.uuid1()

        # The last 10 statement inputs and outputs
        self.conversation = ResponseQueue(maxsize=10)


class SessionManager(object):
    """
    Object to hold and manage multiple chat sessions.
    """

    def __init__(self):
        self.sessions = {}

    def new(self):
        """
        Add a new chat session.
        """
        session = Session()

        self.sessions[session.uuid] = session

        return session

    def get(self, uid):
        """
        Return a session given a unique identifier.
        """
        return self.sessions[uid]

    def get_default(self):
        """
        Return the first and preferably only session.
        """
        if not self.sessions:
            return None

        session_id = list(self.sessions.keys())[0]
        return self.sessions[session_id]

    def update(self, session_id, conversance):
        """
        Add a conversance to a given session if the session exists.
        """
        if session_id in self.sessions:
            self.sessions[session_id].conversation.append(conversance)