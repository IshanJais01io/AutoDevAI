from storage.models import get_last_two_scans


class ComparisonEngine:

    def compare(self):

        scans = get_last_two_scans()

        if len(scans) < 2:

            return {

                "message": "Not enough scans"

            }

        latest = scans[0]

        previous = scans[1]

        return {

            "overall":

                latest[0] - previous[0],

            "security":

                latest[1] - previous[1],

            "testing":

                latest[2] - previous[2],

            "documentation":

                latest[3] - previous[3],

            "latest_date":

                latest[4],

            "previous_date":

                previous[4]

        }