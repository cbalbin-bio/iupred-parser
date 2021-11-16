# Copyright (c) 2021 Christian Balbin
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.


from dataclasses import dataclass


@dataclass
class IUPREDSeq:
    title: str
    pos: list[int]
    amino_acid: list[str]
    iupred_score: list[float]
    anchor_score: list[float]


def IUPREDParser(path):

    with open(path) as results:

        for line in results:
            if line[0] == ">":
                title = line[1:].strip()
                break

        pos = []
        amino_acid = []
        iupred_score = []
        anchor_score = []

        for line in results:
            if line[0] == "#" or line == "\n":
                continue
            elif line[0] == ">":
                yield IUPREDSeq(title, pos, amino_acid, iupred_score, anchor_score)
                title = line[1:].strip()
                pos = []
                amino_acid = []
                iupred_score = []
                anchor_score = []

            else:
                line = line.split("\t")
                pos.append(int(line[0]))
                amino_acid.append(line[1])
                iupred_score.append(float(line[2]))
                anchor_score.append(float(line[3]))

        yield IUPREDSeq(title, pos, amino_acid, iupred_score, anchor_score)


if __name__ == "__main__":
    for iupred_seq in IUPREDParser("iupred/elm_instances_1.result"):
        print(iupred_seq)
        break
