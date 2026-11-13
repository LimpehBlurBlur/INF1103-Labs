class Supplier:
    def __init__(self, supplier_id:int, name:str, contact_email: str):
        self.__supplier_id: int=supplier_id
        self.__name: str=name
        self.__contact_email:str = contact_email

    def display_information(self) -> None:
        print("Supplier ID:",self.__supplier_id)
        print("Supplier:",self.__name)
        print("email:",self.__contact_email)

