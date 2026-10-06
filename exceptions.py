class PetsError(Exception): pass


class ValidationError(PetsError): pass


class NotFoundError(PetsError): pass


class StorageError(PetsError): pass
