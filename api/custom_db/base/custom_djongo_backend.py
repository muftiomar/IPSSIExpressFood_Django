from djongo.base import DatabaseWrapper as DjongoDatabaseWrapper

class DatabaseWrapper(DjongoDatabaseWrapper):
    def _close(self):
        # Override the _close method to prevent the NotImplementedError
        if self.connection is not None:
            try:
                self.connection.close()
            except NotImplementedError:
                # Catch the NotImplementedError and safely ignore it
                pass
