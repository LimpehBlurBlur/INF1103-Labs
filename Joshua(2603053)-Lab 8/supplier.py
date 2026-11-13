class Supplier:
    def __init__(self, supplier_id:str, name:str, contact_email: str):
        self.__supplier_id: str=supplier_id
        self.__name: str=name
        self.__contact_email:str = contact_email

    def display_information(self) -> None:
        print("Supplier Short UEN:",self.__supplier_id)
        print("Supplier:",self.__name)
        print("email:",self.__contact_email)

    def to_dict(self) -> dict:
        return {"id": self.__supplier_id, "name": self.__name, "email": self.__contact_email}

