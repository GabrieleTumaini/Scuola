from typing import List


class Studente:
    def __init__(self, nome: str, cognome: str, eta: int, citta: str) -> None:
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta = citta

    def classificazione(self) -> str:
        if 14 <= self.eta <= 16:
            return "Biennio"
        if 17 <= self.eta <= 19:
            return "Triennio"
        return "Altro"

    def __str__(self) -> str:
        return f"{self.nome} {self.cognome}, {self.eta} anni, residente a {self.citta}"

class Classe:
    def __init__(self, sezione: str, anno: int) -> None:
        self.sezione = sezione
        self.anno = anno
        self.studenti = []

    def aggiungi_studente(self, studente: Studente) -> None:
        self.studenti.append(studente)

    def elenco(self) -> List[Studente]:
        return self.studenti

class Scuola:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.studenti = []

    def aggiungi_studente(self, studente: Studente) -> None:
        self.studenti.append(studente)

    def cerca_per_cognome(self, cognome: str) -> List[Studente]:
        cognome = cognome.lower()
        return [studente for studente in self.studenti if studente.cognome.lower() == cognome]

    def cerca_per_eta(self, eta: int) -> List[Studente]:
        return [studente for studente in self.studenti if studente.eta == eta]

    def conta_studenti(self) -> int:
        return len(self.studenti)

    def __len__(self) -> int:
        return self.conta_studenti()
