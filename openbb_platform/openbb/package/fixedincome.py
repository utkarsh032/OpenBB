### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

import datetime
from typing import List, Literal, Optional, Union

from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.decorators import validate
from openbb_core.app.static.filters import filter_inputs
from openbb_core.provider.abstract.data import Data
from typing_extensions import Annotated


class ROUTER_fixedincome(Container):
    """/fixedincome
    /corporate
    /government
    /rate
    sofr
    /spreads
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
    def corporate(self):  # route = "/fixedincome/corporate"
        from . import fixedincome_corporate

        return fixedincome_corporate.ROUTER_fixedincome_corporate(
            command_runner=self._command_runner
        )

    @property
    def government(self):  # route = "/fixedincome/government"
        from . import fixedincome_government

        return fixedincome_government.ROUTER_fixedincome_government(
            command_runner=self._command_runner
        )

    @property
    def rate(self):  # route = "/fixedincome/rate"
        from . import fixedincome_rate

        return fixedincome_rate.ROUTER_fixedincome_rate(
            command_runner=self._command_runner
        )

    @validate
    def sofr(
        self,
        start_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        end_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="End date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        provider: Optional[Literal["fred"]] = None,
        **kwargs
    ) -> OBBject[List[Data]]:
        """Secured Overnight Financing Rate.

            The Secured Overnight Financing Rate (SOFR) is a broad measure of the cost of
            borrowing cash overnight collateralizing by Treasury securities.


        Parameters
        ----------
        start_date : Optional[datetime.date]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Optional[datetime.date]
            End date of the data, in YYYY-MM-DD format.
        provider : Optional[Literal['fred']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fred' if there is
            no default.
        period : Literal['overnight', '30_day', '90_day', '180_day', 'index']
            Period of SOFR rate. (provider: fred)

        Returns
        -------
        OBBject
            results : List[SOFR]
                Serializable results.
            provider : Optional[Literal['fred']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        SOFR
        ----
        date : date
            The date of the data.
        rate : Optional[float]
            SOFR rate.

        Example
        -------
        >>> from openbb import obb
        >>> obb.fixedincome.sofr()
        """  # noqa: E501

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "start_date": start_date,
                "end_date": end_date,
            },
            extra_params=kwargs,
        )

        return self._run(
            "/fixedincome/sofr",
            **inputs,
        )

    @property
    def spreads(self):  # route = "/fixedincome/spreads"
        from . import fixedincome_spreads

        return fixedincome_spreads.ROUTER_fixedincome_spreads(
            command_runner=self._command_runner
        )